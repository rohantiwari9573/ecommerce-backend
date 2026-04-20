from fastapi import HTTPException, Request
from app.core.redis import redis_client


async def rate_limiter(request: Request):
    client_ip = request.client.host
    key = f"rate_limit:{client_ip}"

    # increment request count
    current = redis_client.incr(key)

    # set expiry on first request
    if current == 1:
        redis_client.expire(key, 60)

    # block if exceeded
    if current > 10:
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Try again later."
        )