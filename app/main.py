from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Database
from app.database import engine, Base

# Routers
from app.routers import user as user_router
from app.routers import product as product_router
from app.routers import cart as cart_router
from app.routers import order as order_router

# Create tables
Base.metadata.create_all(bind=engine)

# App instance
app = FastAPI()


# ✅ Landing Page (Improved UI)
@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>E-commerce Backend API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #0f172a;
                    color: white;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    font-size: 40px;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 18px;
                    color: #cbd5f5;
                }
                .btn {
                    display: inline-block;
                    margin: 20px;
                    padding: 12px 25px;
                    background-color: #3b82f6;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-size: 16px;
                }
                .btn:hover {
                    background-color: #2563eb;
                }
                .links {
                    margin-top: 30px;
                }
                .links a {
                    color: #93c5fd;
                    margin: 0 10px;
                    text-decoration: none;
                }
            </style>
        </head>
        <body>
            <h1>🚀 E-commerce Backend API</h1>
            <p>Built using FastAPI, PostgreSQL, JWT Authentication</p>

            <a class="btn" href="/docs">View API Documentation</a>

            <div class="links">
                <p>Explore more:</p>
                <a href="https://github.com/rohantiwari9573/ecommerce-backend">GitHub</a> |
                <a href="https://www.linkedin.com/in/rohan-tiwari-012106283">LinkedIn</a>
            </div>
        </body>
    </html>
    """


# ✅ Include Routers
app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
app.include_router(order_router.router)