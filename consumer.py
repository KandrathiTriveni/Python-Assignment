import json
import pika

from config import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USER,
    RABBITMQ_PASSWORD,
    QUEUE_NAME,
)

from database import SessionLocal
from models import Item


def callback(ch, method, properties, body):
    data = json.loads(body)

    session = SessionLocal()

    try:
        item = session.query(Item).filter(
            Item.id == data["id"]
        ).first()

        if item:
            item.status = "completed"
            session.commit()
            print(f"Processed: {item.item}")

    except Exception as e:
        session.rollback()
        print(e)

    finally:
        session.close()

    ch.basic_ack(delivery_tag=method.delivery_tag)


credentials = pika.PlainCredentials(
    RABBITMQ_USER,
    RABBITMQ_PASSWORD
)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=credentials
    )
)

channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME, durable=True)

channel.basic_consume(
    queue=QUEUE_NAME,
    on_message_callback=callback
)

print("Waiting for messages...")
channel.start_consuming()