import redis
from app.core.config import settings

# ✅ THIS IS REAL REDIS CLIENT
redis_client = redis.Redis.from_url(
    settings.REDIS_URL,
    decode_responses=True
)