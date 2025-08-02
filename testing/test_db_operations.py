# test_db_operations.py
import pytest
from app.db.mongo import db

@pytest.fixture
def sample_ride():
    # Adding a sample ride to the database
    ride = {
        "ride_id": "R001",
        "user_id": "U123",
        "driver_id": "D456",
        "pickup_location": {"lat": 12.9716, "lon": 77.5946},  # Bangalore coordinates
        "dropoff_location": {"lat": 12.9353, "lon": 77.6245},
        "pickup_time": "2023-08-02T14:00:00",
        "status": "Completed",
        "wait_time": 15  # minutes
    }
    db.rides.insert_one(ride)
    return ride

def test_fetch_ride_by_id(sample_ride):
    ride = db.rides.find_one({"ride_id": sample_ride["ride_id"]})
    assert ride is not None
    assert ride["ride_id"] == sample_ride["ride_id"]
    assert ride["status"] == "Completed"

def test_fetch_ride_by_user(sample_ride):
    rides = list(db.rides.find({"user_id": sample_ride["user_id"]}))
    assert len(rides) > 0
    assert rides[0]["user_id"] == sample_ride["user_id"]

def test_ride_wait_time(sample_ride):
    ride = db.rides.find_one({"ride_id": sample_ride["ride_id"]})
    assert ride["wait_time"] == 15
