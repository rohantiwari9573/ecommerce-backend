from fastapi import FastAPI

from app.database import engine, Base

# Import models
from app.models import user, product, cart, order

# Import routers
from app.routers import user
from app.routers import product
from app.routers import cart
from app.routers import order

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(user.router)
app.include_router(product.router)
app.include_router(cart.router)
app.include_router(order.router)


@app.get("/")
def root():
    return {"message": "E-Commerce Backend Running"}