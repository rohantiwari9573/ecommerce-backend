# 🛒 E-Commerce Backend (FastAPI + PostgreSQL + Redis + Celery + Docker)

A production-ready e-commerce backend built with a scalable architecture, asynchronous processing, and performance optimizations.

---

## 🚀 Tech Stack

* **FastAPI** — High-performance async API framework
* **PostgreSQL** — Relational database for structured data
* **Redis** — Caching + rate limiting + message broker
* **Celery** — Asynchronous task queue for background jobs
* **Docker & Docker Compose** — Containerized deployment

---

## ✨ Core Features

* 🔐 JWT Authentication (signup/login, protected routes)
* 📦 Product Management (CRUD APIs)
* 🛒 Cart System (add/update/remove items)
* 📑 Order Processing (create orders from cart)
* ⚡ Redis Caching (product endpoints)
* 🚦 Rate Limiting (Redis-based)
* 🔄 Async Order Handling (Celery workers)
* 📜 Request & Response Logging
* ⚙️ Environment-based Configuration (.env)

---

## 🧠 System Architecture

```
Client
   ↓
FastAPI (API Layer)
   ↓
PostgreSQL (Persistent Storage)
   ↓
Redis (Cache + Broker)
   ↓
Celery Worker (Async Tasks)
```

---

## 🔄 Request Flow

### 1. Product Fetch

* Client requests `/products`
* FastAPI checks Redis cache
* If cache miss → fetch from PostgreSQL → store in Redis → return response

### 2. Order Placement

* User places order
* Order stored in PostgreSQL
* Task pushed to Redis queue
* Celery worker processes background tasks

---

## ⚡ Why This Architecture?

* **FastAPI** → async support + high throughput
* **PostgreSQL** → strong consistency for transactions
* **Redis** → reduces DB load + enables rate limiting
* **Celery** → offloads heavy tasks → improves API response time
* **Docker** → ensures environment consistency

---

## 📈 Scalability Considerations

* Horizontal scaling via multiple FastAPI instances
* Redis as centralized cache + broker
* Background workers handle heavy operations asynchronously
* DB load reduced using caching layer

---

## 🧪 Future Improvements

* Payment integration (Stripe/Razorpay)
* Inventory locking to prevent race conditions
* Microservices architecture
* CI/CD pipeline
* Unit & integration testing

---

## 🛠️ Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd E-Commerce
```

### 2. Run with Docker

```bash
docker-compose up --build
```

### 3. Access API Docs

```
http://localhost:8000/docs
```

---

## 📌 Key Highlights

* Designed with **scalability and performance in mind**
* Implements **real-world backend patterns**
* Uses **async + caching + background processing**
