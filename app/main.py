from fastapi import FastAPI
from app.routes import tracking
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Sistema de Tracking Web")

app.include_router(tracking.router, prefix="/api")

# Montar la carpeta 'static' para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")