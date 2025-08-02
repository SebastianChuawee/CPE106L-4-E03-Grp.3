from pydantic import BaseModel, Field
from typing import Optional

class Driver(BaseModel):
    driver_id: str
    name: str
    email: str
    phone: str
    vehicle_type: str
    status: str  # Available, on-ride, offline
    location: tuple  # Coordinates (lat, lon)
    registration_date: str

class DriverCreate(BaseModel):
    name: str
    email: str
    phone: str
    vehicle_type: str
    location: tuple
