import math
from app.db.mongo import db
from app.models.ride import Ride, RideCreate
from app.models.driver import Driver
from typing import List

def haversine(lat1, lon1, lat2, lon2):
    # Haversine formula to calculate distance between two lat-long points
    R = 6371  # Radius of the Earth in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # Returns distance in km

def find_nearest_driver(user_lat, user_lon, ride_type: str) -> Driver:
    available_drivers = db.drivers.find({"status": "Available"})
    nearest_driver = None
    min_distance = float('inf')

    for driver in available_drivers:
        driver_lat, driver_lon = driver["location"]
        distance = haversine(user_lat, user_lon, driver_lat, driver_lon)
        
        # You can add more conditions here, e.g., matching ride type
        if ride_type == "PWD" and driver["vehicle_type"] == "Accessible":
            if distance < min_distance:
                nearest_driver = driver
                min_distance = distance

    return nearest_driver

def create_ride(user_id: str, user_lat: float, user_lon: float, ride_type: str) -> Ride:
    nearest_driver = find_nearest_driver(user_lat, user_lon, ride_type)
    if nearest_driver:
        ride_data = RideCreate(
            user_id=user_id,
            driver_id=nearest_driver["driver_id"],
            pickup_location=(user_lat, user_lon),
            dropoff_location=(user_lat + 0.05, user_lon + 0.05),  # Placeholder
            pickup_time="2025-08-02T12:00:00",  # Example pickup time
            ride_type=ride_type
        )

        # Save ride to the database
        ride_id = str(uuid.uuid4())
        ride = Ride(ride_id=ride_id, **ride_data.dict())
        db.rides.insert_one(ride.dict())
        return ride

    return None
