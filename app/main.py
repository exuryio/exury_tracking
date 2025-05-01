from fastapi import FastAPI
from app.routes import tracking
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Sistema de Tracking Web")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://exurydev--pr53-feature-tracking-geo-vlstfn0l.web.app"
    ],  # Aquí puedes añadir más orígenes si los necesitas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raíz
@app.get("/")
def read_root():
    return {"message": "Bienvenido al sistema de tracking de Exury"}

# Incluir las rutas del tracking
app.include_router(tracking.router, prefix="/api")

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
