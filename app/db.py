from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models.base import Base 


# Definir la URL de la base de datos
DATABASE_URL = "postgresql://exury:1017@localhost/exury_tracking_db"  

# Crear el engine con la URL de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Crear todas las tablas si no existen
Base.metadata.create_all(bind=engine)

# Crear la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
