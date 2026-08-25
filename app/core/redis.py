import redis
from redis.backoff import NoBackoff
from redis.retry import Retry
from app.core.config import settings

# Short timeout, no retries: an unreachable Redis fails fast instead of stalling requests
redis_client = redis.Redis.from_url(
    settings.REDIS_URL,
    decode_responses=True,
    socket_connect_timeout=2,
    socket_timeout=2,
    retry=Retry(NoBackoff(), 0),
)
