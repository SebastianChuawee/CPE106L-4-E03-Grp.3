from fastapi import APIRouter, HTTPException
from app.models.user import UserCreate, User
from app.db.mongo import db
from app.schemas.user_schema import User
from app.utils.auth_utils import hash_password
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/register_user")
async def register_user(user: UserCreate):
    user_id = str(uuid.uuid4())
    user_data = User(
        user_id=user_id,
        name=user.name,
        email=user.email,
        phone=user.phone,
        address=user.address,
        is_eld=user.is_eld,
        is_pwd=user.is_pwd,
        registration_date=datetime.now().isoformat()
    )
    try:
        db.users.insert_one(user_data.dict())
        return {"message": "User registered successfully", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/register_driver")
async def register_driver(driver: DriverCreate):
    driver_id = str(uuid.uuid4())
    driver_data = Driver(
        driver_id=driver_id,
        name=driver.name,
        email=driver.email,
        phone=driver.phone,
        vehicle_type=driver.vehicle_type,
        status="Available",
        location=driver.location,
        registration_date=datetime.now().isoformat()
    )
    try:
        db.drivers.insert_one(driver_data.dict())
        return {"message": "Driver registered successfully", "driver_id": driver_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
