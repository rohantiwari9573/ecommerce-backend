from fastapi import FastAPI

from app.database import engine, Base

# Import all models
from app.models import user, product, cart, order

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "E-Commerce Backend Running"}