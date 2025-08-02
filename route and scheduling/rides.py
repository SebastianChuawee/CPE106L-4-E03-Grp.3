from fastapi import APIRouter, HTTPException
from app.services.ride_service import create_ride
from app.models.ride import RideCreate

router = APIRouter()

@router.post("/request_ride")
async def request_ride(ride_request: RideCreate):
    user_lat = ride_request.pickup_location[0]
    user_lon = ride_request.pickup_location[1]
    ride = create_ride(ride_request.user_id, user_lat, user_lon, ride_request.ride_type)
    
    if ride:
        return {"message": "Ride requested successfully", "ride_id": ride.ride_id}
    else:
        raise HTTPException(status_code=404, detail="No available driver found")

@router.get("/ride_route/{ride_id}")
async def get_ride_route(ride_id: str):
    ride = db.rides.find_one({"ride_id": ride_id})
    if ride:
        get_route_for_ride(ride) 
        return {"ride_id": ride_id, "distance": ride["distance"], "estimated_time": ride["estimated_time"]}
    else:
        raise HTTPException(status_code=404, detail="Ride not found")
