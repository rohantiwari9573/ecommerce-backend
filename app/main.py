from fastapi import FastAPI, Request, Depends
from app.database import engine, Base
from app.routers import user, product, cart, order
from app.core.rate_limiter import rate_limiter
from app.core.logger import logger

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)


# 🔥 LOGGING MIDDLEWARE
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")

    response = await call_next(request)

    logger.info(f"Response status: {response.status_code}")

    return response


# include routers with rate limiting
app.include_router(user.router, dependencies=[Depends(rate_limiter)])
app.include_router(product.router, dependencies=[Depends(rate_limiter)])
app.include_router(cart.router, dependencies=[Depends(rate_limiter)])
app.include_router(order.router, dependencies=[Depends(rate_limiter)])


@app.get("/")
def root():
    return {"message": "E-commerce API is running"}