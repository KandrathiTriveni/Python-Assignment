
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672
RABBITMQ_USER = "guest"
RABBITMQ_PASSWORD = "guest"
QUEUE_NAME = "items_queue"

DATABASE_URL = "sqlite:///items.db"


SECRET_KEY = "routemobile"


CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"
CELERY_RESULT_BACKEND = "rpc://"