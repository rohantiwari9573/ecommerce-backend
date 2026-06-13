from fastapi import FastAPI

from app.database import engine, Base

# Import models
from app.models import user, product, cart, order

# Import routers
from app.routes import user_routes
from app.routes import product_routes
from app.routes import cart_routes
from app.routes import order_routes

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(user_routes.router)
app.include_router(product_routes.router)
app.include_router(cart_routes.router)
app.include_router(order_routes.router)


@app.get("/")
def root():
    return {"message": "E-Commerce Backend Running"}