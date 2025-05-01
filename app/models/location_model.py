from sqlalchemy import Column, Float, String, Integer
from app.models.base import Base


class LocationModel(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    address = Column(String)
