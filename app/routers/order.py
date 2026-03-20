from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.cart import Cart
from app.models.product import Product
from app.models.user import User
from app.schemas.order import OrderResponse
from app.dependencies import get_db
from app.auth.utils import get_current_user

router = APIRouter()


# 🧾 CREATE ORDER (CHECKOUT)
@router.post("/orders", response_model=OrderResponse)
def create_order(
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    email = user.get("sub")

    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    cart_items = db.query(Cart).filter(Cart.user_id == db_user.id).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total_price = 0

    # Calculate total
    for item in cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            continue
        total_price += product.price

    # Create order
    new_order = Order(
        user_id=db_user.id,
        total_price=total_price
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    # Create order items
    for item in cart_items:
        order_item = OrderItem(
            order_id=new_order.id,
            product_id=item.product_id
        )
        db.add(order_item)

    # Clear cart
    for item in cart_items:
        db.delete(item)

    db.commit()

    return new_order


# 📦 GET USER ORDERS
@router.get("/orders")
def get_orders(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    email = user

    db_user = db.query(User).filter(User.email == email).first()

    orders = db.query(Order).filter(Order.user_id == db_user.id).all()

    result = []

    for order in orders:
        order_items = db.query(OrderItem).filter(OrderItem.order_id == order.id).all()

        items = []

        for item in order_items:
            product = db.query(Product).filter(Product.id == item.product_id).first()

            items.append({
                "product_id": product.id,
                "name": product.name,
                "price": product.price
            })

        result.append({
            "id": order.id,
            "total_price": order.total_price,
            "items": items
        })

    return result