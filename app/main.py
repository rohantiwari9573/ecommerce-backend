from fastapi import FastAPI, Request, Depends

from app.database import engine, Base
from app.core.rate_limiter import rate_limiter
from app.core.logger import logger

# Import models so they register with SQLAlchemy's Base metadata
from app.models import user as user_model
from app.models import product as product_model
from app.models import cart as cart_model
from app.models import order as order_model
from app.models import order_item as order_item_model

# Import routers
from app.routers import user, product, cart, order

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce Backend API",
    description="Products, carts and orders with JWT auth, Redis caching and rate limiting, and Celery background jobs.",
    version="1.0.0",
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")

    response = await call_next(request)

    logger.info(f"Response status: {response.status_code}")

    return response


# Include routers with rate limiting
app.include_router(user.router, dependencies=[Depends(rate_limiter)])
app.include_router(product.router, dependencies=[Depends(rate_limiter)])
app.include_router(cart.router, dependencies=[Depends(rate_limiter)])
app.include_router(order.router, dependencies=[Depends(rate_limiter)])


@app.get("/")
def root():
    return {"message": "E-Commerce Backend Running"}


# Liveness probe for uptime pingers: registered on the app (not a router), so
# the per-router rate limiter doesn't apply; no auth and no database access.
@app.get("/health")
def health():
    return {"status": "healthy"}


# TEMPORARY: reveals how the hosting proxy forwards client IPs. Removed in
# the follow-up commit once the rate limiter is fixed.
@app.get("/_debug/client-ip", include_in_schema=False)
def debug_client_ip(request: Request):
    keys = ("x-forwarded-for", "x-real-ip", "true-client-ip", "cf-connecting-ip", "forwarded", "x-forwarded-proto", "via", "cf-ray", "rndr-id")
    return {"client_host": request.client.host if request.client else None, **{k: request.headers.get(k) for k in keys}}
