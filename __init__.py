
from fastapi import FastAPI
from . import db
from . import auth
from . import models
from . import ride_scheduler

# Initialize the FastAPI app here
app = FastAPI()

# You can add background tasks, event handlers, etc.
@app.on_event("startup")
async def startup_event():
    print("Starting the app...")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down the app...")
