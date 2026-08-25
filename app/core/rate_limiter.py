from fastapi import HTTPException, Request
from app.core.redis import redis_client
from app.core.logger import logger


# Sync def: FastAPI runs sync dependencies in a threadpool, so a slow/unreachable
# Redis blocks only the calling request's worker thread, not the whole event loop.
def rate_limiter(request: Request):
    client_ip = request.client.host
    key = f"rate_limit:{client_ip}"

    try:
        current = redis_client.incr(key)

        # set expiry on first request
        if current == 1:
            redis_client.expire(key, 60)
    except Exception as exc:
        # Redis unavailable — fail open rather than take down every request
        logger.warning(f"Rate limiter unavailable, allowing request: {exc}")
        return

    # block if exceeded
    if current > 10:
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Try again later."
        )
