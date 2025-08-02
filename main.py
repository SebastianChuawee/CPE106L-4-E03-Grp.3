from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.db.mongo import db
from app.auth import authenticate_user, create_access_token, get_current_user
from app.models import Ride, User, Driver
from app.ride_scheduler import match_ride, calculate_route
import datetime

# Initialize FastAPI
app = FastAPI()

# Models for request bodies
class RideRequest(BaseModel):
    user_id: str
    driver_id: str
    pickup_location: dict
    dropoff_location: dict
    pickup_time: datetime.datetime
    status: str = "Pending"
    wait_time: int = 0

class UserRequest(BaseModel):
    email: str
    password: str

# API Routes

# 1. User Registration (For new users)
@app.post("/register_user")
async def register_user(user_request: UserRequest):
    user = User(**user_request.dict())
    db.users.insert_one(user.dict())
    return {"message": "User registered successfully."}

# 2. Driver Registration (For new drivers)
@app.post("/register_driver")
async def register_driver(user_request: UserRequest):
    driver = Driver(**user_request.dict())
    db.drivers.insert_one(driver.dict())
    return {"message": "Driver registered successfully."}

# 3. User Login (JWT token-based)
@app.post("/login")
async def login(user_request: UserRequest):
    user = db.users.find_one({"email": user_request.email})
    if not user or not authenticate_user(user, user_request.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user_request.email})
    return {"access_token": access_token, "token_type": "bearer"}

# 4. Ride Booking
@app.post("/book_ride")
async def book_ride(ride_request: RideRequest, current_user: str = Depends(get_current_user)):
    user = db.users.find_one({"email": current_user})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    driver = db.drivers.find_one({"driver_id": ride_request.driver_id})
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    
    # Match user to a driver based on proximity or availability
    matched_ride = match_ride(user, driver)
    if not matched_ride:
        raise HTTPException(status_code=400, detail="No available driver for this ride")
    
    ride_data = Ride(**ride_request.dict(), matched_ride=matched_ride)
    db.rides.insert_one(ride_data.dict())
    
    return {"message": "Ride booked successfully", "ride_id": ride_data.ride_id}

# 5. Update Ride Status (e.g., Completed, Cancelled)
@app.put("/update_ride_status/{ride_id}")
async def update_ride_status(ride_id: str, status: str):
    ride = db.rides.find_one({"ride_id": ride_id})
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    
    db.rides.update_one({"ride_id": ride_id}, {"$set": {"status": status}})
    return {"message": f"Ride status updated to {status}"}

# 6. Get Ride History for a User
@app.get("/ride_history/{user_id}")
async def get_ride_history(user_id: str):
    rides = list(db.rides.find({"user_id": user_id}))
    if not rides:
        raise HTTPException(status_code=404, detail="No ride history found for this user")
    return {"rides": rides}

# 7. Route Calculation (Google Maps integration can be implemented here)
@app.get("/calculate_route")
async def calculate_route_endpoint(pickup_location: dict, dropoff_location: dict):
    route = calculate_route(pickup_location, dropoff_location)
    return {"route": route}

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Accessible Transportation Scheduler!"}
