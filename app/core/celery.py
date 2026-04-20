from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

# ✅ EXPLICIT IMPORT (FORCES REGISTRATION)
import app.tasks.order_tasks

celery_app.conf.task_routes = {
    "app.tasks.*": {"queue": "default"}
}