from fastapi import FastAPI
from app.routers import cart
from app.database import engine, Base
from app.routers.order import router as order_router

from app.models import product
from app.models import user


from app.routers.product import router as product_router
from app.routers import user as user_router

app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(order_router)
app.include_router(product_router)
app.include_router(user_router.router)
app.include_router(cart.router)

@app.get("/")
def root():
    return {"message": "E-commerce backend running"}
