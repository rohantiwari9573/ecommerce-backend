from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.cart import Cart
from app.models.user import User
from app.models.product import Product
from app.schemas.cart import CartCreate
from app.dependencies import get_db
from app.auth.utils import get_current_user

router = APIRouter()


# 🛒 ADD TO CART
@router.post("/cart")
def add_to_cart(
    cart: CartCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    email = user

    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    product = db.query(Product).filter(Product.id == cart.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    new_cart_item = Cart(
        user_id=db_user.id,
        product_id=cart.product_id
    )

    db.add(new_cart_item)
    db.commit()
    db.refresh(new_cart_item)

    return {"message": "Product added to cart"}


# 📦 GET CART (UPDATED WITH PRODUCT DETAILS)
@router.get("/cart")
def get_cart(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    email = user

    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    cart_items = db.query(Cart).filter(Cart.user_id == db_user.id).all()

    response = []

    for item in cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()

        if product:
            response.append({
                "id": item.id,
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price
                }
            })

    return response


# ❌ REMOVE FROM CART
@router.delete("/cart/{product_id}")
def remove_from_cart(
    product_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    email = user

    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    cart_item = db.query(Cart).filter(
        Cart.user_id == db_user.id,
        Cart.product_id == product_id
    ).first()

    if not cart_item:
        raise HTTPException(status_code=404, detail="Item not in cart")

    db.delete(cart_item)
    db.commit()

    return {"message": "Item removed from cart"}