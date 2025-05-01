# endpoints 
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.location_model import LocationModel  # Importar el modelo de la base de datos
from app.db import get_db  # Importar la función para obtener la conexión a la base de datos
from app.models.location import Location  # El modelo Pydantic para validar la entrada
from app.utils.geolocation import get_address  # Función para obtener la dirección

router = APIRouter()

@router.post("/track")
async def track_location(location: Location, db: Session = Depends(get_db)):
    try:
        # Obtener la dirección usando latitud y longitud
        address = get_address(location.latitude, location.longitude)

        # Crear un nuevo objeto LocationModel para almacenar la ubicación en la base de datos
        new_location = LocationModel(
            latitude=location.latitude,
            longitude=location.longitude,
            address=address
        )

        # Guardar la ubicación en la base de datos
        db.add(new_location)
        db.commit()

        return {"message": "Ubicación recibida y almacenada", "address": address}
    
    except Exception as e:
        db.rollback()  # Si hay algún error, revertir la transacción
        raise HTTPException(status_code=400, detail=f"Error al registrar ubicación: {str(e)}")
