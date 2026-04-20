from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.cart import Cart
from app.models.product import Product
from app.models.user import User
from app.schemas.cart import CartCreate
from app.dependencies import get_db
from app.auth.utils import get_current_user

router = APIRouter()


# 🛒 ADD TO CART
@router.post("/cart")
def add_to_cart(
    cart: CartCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    # ✅ FIX HERE
    email = user.get("sub")

    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")

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

    return {"message": "Item added to cart"}


# 🛒 GET CART
@router.get("/cart")
def get_cart(
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    # ✅ FIX HERE
    email = user.get("sub")

    db_user = db.query(User).filter(User.email == email).first()

    cart_items = db.query(Cart).filter(Cart.user_id == db_user.id).all()

    result = []

    for item in cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()

        if product:
            result.append({
                "product_id": product.id,
                "name": product.name,
                "price": product.price
            })

    return result