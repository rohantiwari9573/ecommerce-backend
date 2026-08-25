# 🛒 Scalable E-Commerce Backend System

A production-style e-commerce backend built using FastAPI with asynchronous processing, Redis-powered optimizations, Dockerized services, and CI/CD integration.

---

# 🚀 Live Deployment

API Docs:

https://ecommerce-backend-spj8.onrender.com/docs

---

# 🚀 Tech Stack

* **FastAPI** — High-performance async API framework
* **PostgreSQL / SQLite** — Relational database management
* **SQLAlchemy** — ORM for database abstraction
* **Redis** — Caching, rate limiting, and Celery broker
* **Celery** — Asynchronous task processing (fully async processing runs via Docker Compose locally)
* **Docker & Docker Compose** — Multi-container architecture
* **GitHub Actions** — Continuous Integration (CI)
* **Render** — Cloud deployment platform

---

# ✨ Core Features

* 🔐 JWT Authentication (signup/login + protected routes)
* 📦 Product Management APIs
* 🛒 Cart Management System
* 📑 Order Creation Workflow
* ⚡ Redis-based Product Caching
* 🚦 API Rate Limiting using Redis
* 🔄 Asynchronous Background Task Architecture using Celery
* 📜 Automatic Swagger/OpenAPI Documentation
* ⚙️ Environment-based Configuration using `.env`
* 🐳 Dockerized Multi-Service Deployment
* 🔁 CI Pipeline using GitHub Actions

---

# 🧠 System Architecture

```text
Client
   ↓
FastAPI (API Layer)
   ↓
PostgreSQL / SQLite
   ↓
Redis (Caching + Broker)
   ↓
Celery Worker (Async Processing)
```

---

# 🔄 Request Flow

## 1. Product Fetch Workflow

* Client requests `/products`
* FastAPI checks Redis cache
* On cache miss:

  * fetches data from database
  * stores response in Redis
  * returns optimized response

---

## 2. Order Placement Workflow

* User authenticates using JWT token
* Items added to cart
* Order created from cart items
* Celery task can process background operations asynchronously

---

# ⚡ Performance & Scalability Features

* Redis caching reduces repeated database queries
* Rate limiting protects APIs from abuse
* Background task architecture improves responsiveness
* Modular router-based architecture improves maintainability
* Dockerized services ensure reproducible environments
* CI pipeline automates validation during code pushes

---

# 🚀 CI/CD Pipeline

Implemented Continuous Integration using GitHub Actions.

Pipeline automatically:

* installs dependencies
* validates Python syntax
* builds Docker image
* runs on every push to `main`

---

# ☁️ Deployment

The backend is deployed on Render using environment-based configuration variables.

Deployment includes:

* FastAPI API server
* Swagger documentation
* Cloud-hosted REST endpoints

---

# 🛠️ Local Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/rohantiwari9573/ecommerce-backend.git
cd ecommerce-backend
```

---

## 2. Configure Environment Variables

Create `.env` file:

```env
SECRET_KEY=mysecretkey
DATABASE_URL=postgresql://postgres:admin123@db:5432/ecommerce
REDIS_URL=redis://redis:6379/0
```

---

## 3. Run with Docker

```bash
docker-compose up --build
```

---

## 4. Access Swagger Docs

```text
http://localhost:8000/docs
```

---

# 📌 Key Engineering Concepts Covered

* REST API Design
* JWT Authentication
* Database ORM Modeling
* Redis Caching
* Rate Limiting
* Asynchronous Task Queues
* Docker Containerization
* Multi-Service Architecture
* CI/CD Pipelines
* Cloud Deployment

---

# 👨‍💻 Author

Rohan Tiwari

GitHub:
https://github.com/rohantiwari9573

LinkedIn:
https://www.linkedin.com/in/rohan-tiwari-012106283/
