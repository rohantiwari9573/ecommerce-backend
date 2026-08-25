import redis
from redis.backoff import NoBackoff
from redis.retry import Retry
from app.core.config import settings

# Short timeout, no retries: an unreachable Redis fails fast instead of stalling
# requests. redis-py applies this timeout at two layers (connection setup and
# command execution) even with retries disabled, so real failure latency is
# ~2x this value per Redis call — measured ~1s at 0.5s. 0.5s comfortably
# covers a real network round trip while keeping worst-case fallback latency
# low on endpoints that touch Redis more than once (e.g. GET /products).
redis_client = redis.Redis.from_url(
    settings.REDIS_URL,
    decode_responses=True,
    socket_connect_timeout=0.5,
    socket_timeout=0.5,
    retry=Retry(NoBackoff(), 0),
)
