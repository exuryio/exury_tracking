from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models.base import Base 


# Definir la URL de la base de datos
DATABASE_URL = "postgresql://tracking_db_te1b_user:ORnC0nZczdLXOJXCUSMnsc9fiC3WcxPi@dpg-d09r83ili9vc73aq87o0-a.frankfurt-postgres.render.com/tracking_db_te1b"  

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
