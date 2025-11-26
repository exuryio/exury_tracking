# 🚀 FastAPI Backend -- PostgreSQL, SQLAlchemy & Prometheus Metrics

A high-performance **FastAPI** backend powered by **Uvicorn**,
**SQLAlchemy**, and **PostgreSQL**, with integrated **Prometheus
metrics** for monitoring and health insights.

The application is designed for production environments such as
**Heroku**, **Railway**, or any container-based deployment platform.\
Environment variables are managed through **python-dotenv**.

------------------------------------------------------------------------

## ✨ Features

-   ⚡ Ultra-fast API built with FastAPI\
-   🐘 PostgreSQL database support via SQLAlchemy + psycopg2\
-   📦 Pydantic models for validation\
-   📡 Async-compatible HTTP libraries: httpx & requests\
-   📊 Prometheus metrics (prometheus-fastapi-instrumentator)\
-   🔧 Environment variable support via .env\
-   🚀 Production-ready Procfile\
-   🧱 Clean project structure

------------------------------------------------------------------------

## 📂 Project Structure

    /app
      /routers
      /models
      /schemas
      /services
      /database
      main.py
    .env
    requirements.txt
    Procfile

------------------------------------------------------------------------

## 🔧 Requirements

Install dependencies:

``` bash
pip install -r requirements.txt
```

Included packages:

-   fastapi\
-   uvicorn\
-   pydantic\
-   sqlalchemy\
-   psycopg2-binary\
-   python-dotenv\
-   prometheus-fastapi-instrumentator\
-   prometheus_client\
-   httpx\
-   requests

------------------------------------------------------------------------

## ⚙️ Environment Variables

Create a `.env` file:

    DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DBNAME
    DEBUG=True
    METRICS_ENABLED=True
    METRICS_ENDPOINT=/metrics

------------------------------------------------------------------------

## ▶️ Development Server

``` bash
uvicorn app.main:app --reload
```

------------------------------------------------------------------------

## 🚀 Production Deployment

Using **Procfile**:

    web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT}

Deploy on platforms like:

-   Railway\
-   Render\
-   Heroku\
-   Fly.io

------------------------------------------------------------------------

## 📊 Prometheus Metrics

Example integration:

``` python
from prometheus_fastapi_instrumentator import Instrumentator

Instrumentator().instrument(app).expose(app, endpoint="/metrics")
```

Metrics work with:

-   Prometheus\
-   Grafana\
-   Cloud monitoring tools

------------------------------------------------------------------------

## 🛢️ Database (PostgreSQL Example)

``` python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

------------------------------------------------------------------------

## 👤 Author

https://github.com/yizpuentesc
https://github.com/Divisy

------------------------------------------------------------------------

## 📄 License

This project is licensed under the **ISC License**.

------------------------------------------------------------------------

## ⭐ Support

If this project was useful, please consider starring the repository! ⭐
