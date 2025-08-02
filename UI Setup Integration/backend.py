@router.get("/assigned_rides")
async def get_assigned_rides(driver_id: str):
    # Retrieve rides assigned to the driver
    rides = db.rides.find({"driver_id": driver_id})
    return rides
