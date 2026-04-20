from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate
from app.dependencies import get_db
from app.core.redis import redis_client
import json

router = APIRouter()


@router.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        name=product.name,
        price=product.price
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    # ❗ invalidate cache
    redis_client.delete("products")

    return new_product


@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    # 🔥 CHECK CACHE
    cached_products = redis_client.get("products")

    if cached_products:
        return json.loads(cached_products)

    # ❌ CACHE MISS → DB HIT
    products = db.query(Product).all()

    data = [
        {"id": p.id, "name": p.name, "price": p.price}
        for p in products
    ]

    # 🔥 STORE IN REDIS (TTL 60 sec)
    redis_client.setex("products", 60, json.dumps(data))

    return data