from fastapi import APIRouter
from app.models.location import Location
from app.utils.geolocation import get_address

router = APIRouter()

@router.post("/track")
async def track_location(location: Location):
    address = get_address(location.latitude, location.longitude)
    # Aquí puedes almacenar la información en una base de datos
    return {"message": "Ubicación recibida", "address": address}
