from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate
from app.dependencies import get_db

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

    return new_product


@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()

    return [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price
        }
        for p in products
    ]