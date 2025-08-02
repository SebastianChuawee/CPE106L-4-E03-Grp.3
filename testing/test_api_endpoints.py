import pytest
from fastapi.testclient import TestClient
from app.main import app  # Your FastAPI app

client = TestClient(app)

def test_ride_booking():
    ride_payload = {
        "user_id": "U123",
        "driver_id": "D456",
        "pickup_location": {"lat": 12.9716, "lon": 77.5946},
        "dropoff_location": {"lat": 12.9353, "lon": 77.6245},
        "pickup_time": "2023-08-02T14:00:00"
    }
    response = client.post("/book_ride", json=ride_payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Ride booked successfully."

def test_update_ride_status():
    ride_payload = {
        "ride_id": "R001",
        "status": "Completed"
    }
    response = client.put("/update_ride_status/R001", json=ride_payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Ride status updated"
