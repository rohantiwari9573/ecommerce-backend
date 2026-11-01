from app.database import SessionLocal
from app.models.product import Product
from app.core.logger import logger

# A small starter catalog so the live demo isn't empty. Only inserted when
# the products table has no rows, so it never duplicates or overwrites data.
DEMO_PRODUCTS = [
    ("Wireless Noise-Cancelling Headphones", 8999.0),
    ("Mechanical Keyboard (TKL, Brown Switches)", 4499.0),
    ("27-inch 4K IPS Monitor", 24999.0),
    ("USB-C 65W GaN Charger", 1799.0),
    ("Ergonomic Office Chair", 12499.0),
    ("Stainless Steel Water Bottle (1L)", 699.0),
    ("Running Shoes", 3299.0),
    ("Backpack with Laptop Sleeve", 2199.0),
]


def seed_demo_products():
    db = SessionLocal()
    try:
        if db.query(Product).first() is None:
            db.add_all(Product(name=name, price=price) for name, price in DEMO_PRODUCTS)
            db.commit()
            logger.info(f"Seeded {len(DEMO_PRODUCTS)} demo products")
    finally:
        db.close()
