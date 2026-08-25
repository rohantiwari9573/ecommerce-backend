import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate
from app.dependencies import get_db
from app.core.redis import redis_client
from app.core.logger import logger

router = APIRouter()

CACHE_KEY = "products"
CACHE_TTL_SECONDS = 60


@router.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        name=product.name,
        price=product.price
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    try:
        redis_client.delete(CACHE_KEY)
    except Exception as exc:
        logger.warning(f"Cache invalidation skipped: {exc}")

    return new_product


@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    try:
        cached_products = redis_client.get(CACHE_KEY)
        if cached_products:
            return json.loads(cached_products)
    except Exception as exc:
        logger.warning(f"Cache read skipped: {exc}")

    products = db.query(Product).all()

    data = [
        {"id": p.id, "name": p.name, "price": p.price}
        for p in products
    ]

    try:
        redis_client.setex(CACHE_KEY, CACHE_TTL_SECONDS, json.dumps(data))
    except Exception as exc:
        logger.warning(f"Cache write skipped: {exc}")

    return data
