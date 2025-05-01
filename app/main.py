from fastapi import FastAPI
from app.routes import tracking
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Sistema de Tracking Web")

# Endpoint raíz para que no de 404 en "/"
@app.get("/")
def read_root():
    return {"message": "Bienvenido al sistema de tracking de Exury"}

# Incluir las rutas del tracking
app.include_router(tracking.router, prefix="/api")

# Montar la carpeta 'static' para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
