# E-Commerce Backend (FastAPI + PostgreSQL + Redis + Celery + Docker)

A production-style e-commerce backend with JWT auth, caching, rate limiting, and asynchronous order processing.

## Tech Stack
- FastAPI, SQLAlchemy
- PostgreSQL
- Redis (cache + broker)
- Celery (background tasks)
- Docker & Docker Compose

## Features
- JWT Authentication (signup/login, protected routes)
- Products, Cart, Orders
- Redis caching for /products
- Rate limiting (Redis)
- Async order processing via Celery
- Environment-based config (.env)
- Request/response logging

## Architecture
FastAPI → PostgreSQL  
FastAPI → Redis → Celery Worker

## Getting Started

### 1. Clone
```bash
git clone <your-repo-url>
cd E-Commerce