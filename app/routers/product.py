from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.product import ProductCreate, ProductResponse
from app.models.product import Product as ProductModel
from app.dependencies import get_db
from app.auth.utils import get_current_user

router = APIRouter()


# CREATE PRODUCT
@router.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = ProductModel(
        name=product.name,
        price=product.price
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


# GET ALL PRODUCTS (PROTECTED)
@router.get("/products", response_model=list[ProductResponse])
def get_products(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return db.query(ProductModel).all()


# GET PRODUCT BY ID
@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


# UPDATE PRODUCT
@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, updated_product: ProductCreate, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = updated_product.name
    product.price = updated_product.price

    db.commit()
    db.refresh(product)

    return product


# DELETE PRODUCT
@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}