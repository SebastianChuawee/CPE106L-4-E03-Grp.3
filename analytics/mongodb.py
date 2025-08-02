from app.db.mongo import db
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Get all completed rides from MongoDB
def get_ride_data():
    rides = db.rides.find({"status": "Completed"})
    ride_data = []
    for ride in rides:
        ride_data.append({
            "pickup_time": datetime.strptime(ride["pickup_time"], "%Y-%m-%dT%H:%M:%S"),
            "wait_time": ride["wait_time"],  # Assuming this field exists in your database
            "user_location": ride["pickup_location"],  # Assuming it's a (lat, lon) tuple
            "dropoff_location": ride["dropoff_location"]
        })
    return ride_data
