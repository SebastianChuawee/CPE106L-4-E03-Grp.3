from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json
from typing import List

app = FastAPI()

# A list to hold all connected WebSocket clients
active_connections: List[WebSocket] = []

# A function to broadcast updates to all connected clients
async def broadcast(message: str):
    for connection in active_connections:
        await connection.send_text(message)

@app.websocket("/ws/ride_updates/{user_id}")
async def websocket_ride_updates(websocket: WebSocket, user_id: str):
    # Accept the connection
    await websocket.accept()
    active_connections.append(websocket)

    try:
        while True:
            # Keep the connection open and wait for messages
            data = await websocket.receive_text()
            print(f"Message from {user_id}: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        print(f"Client {user_id} disconnected")

@app.put("/update_ride_status/{ride_id}")
async def update_ride_status(ride_id: str, status: str):
    # Update ride status in the database
    ride = db.rides.find_one({"ride_id": ride_id})
    if ride:
        # Simulate a ride status update (this could be more complex)
        db.rides.update_one({"ride_id": ride_id}, {"$set": {"status": status}})
        # Notify all connected clients
        message = json.dumps({"ride_id": ride_id, "status": status})
        await broadcast(message)
        return {"message": "Ride status updated", "ride_id": ride_id}
    return {"message": "Ride not found", "status": 404}
