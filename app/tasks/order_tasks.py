from app.core.celery import celery_app
import time


@celery_app.task(name="process_order")
def process_order(order_id: int):
    print(f"Processing order {order_id}...")

    time.sleep(5)

    print(f"Order {order_id} processed successfully!")