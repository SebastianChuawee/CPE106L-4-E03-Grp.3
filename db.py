from pymongo import MongoClient

# MongoDB Connection URI
client = MongoClient("mongodb://localhost:27017")
db = client["transportation_scheduler"]

users = db.users
drivers = db.drivers
rides = db.rides
