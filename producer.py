import json
import pika

from config import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USER,
    RABBITMQ_PASSWORD,
    QUEUE_NAME
)

from database import SessionLocal
from models import Item


def send_item(item_name):
    session = SessionLocal()

    try:
        # Insert into database with pending status
        new_item = Item(
            item=item_name,
            status="pending"
        )

        session.add(new_item)
        session.commit()
        session.refresh(new_item)

        # Prepare message
        message = {
            "id": new_item.id,
            "item": new_item.item
        }

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

        channel.queue_declare(
            queue=QUEUE_NAME,
            durable=True
        )

        channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME,
            body=json.dumps(message)
        )

        connection.close()

        return message

    finally:
        session.close()