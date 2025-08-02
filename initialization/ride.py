from pydantic import BaseModel
from typing import Optional

class Ride(BaseModel):
    ride_id: str
    user_id: str
    driver_id: str
    status: str  # Pending, Confirmed, In Progress, Completed
    pickup_location: tuple  # Coordinates (lat, lon)
    dropoff_location: tuple
    pickup_time: str
    ride_type: str  # Elderly or PWD
    distance: float
    estimated_time: float

class RideCreate(BaseModel):
    user_id: str
    driver_id: str
    pickup_location: tuple
    dropoff_location: tuple
    pickup_time: str
    ride_type: str
