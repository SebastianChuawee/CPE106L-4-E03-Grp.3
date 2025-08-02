# 📘 CPE106L-4 | E03 – Laboratory Reports & Project Repository

Welcome to our official repository for **CPE106L-4 | E03** under the **Department of Computer Engineering** at **Mapúa University**. This repository contains our complete submissions for **Lab Exercises 1–7** and our capstone project titled **"ACCESS-RIDE: Smart Scheduler for Inclusive Community Transport"**.

The Laboratory Reports' Source Codes are found in the Lab Report branch of this repository.

---

## 📁 Repository Structure
Each folder under `labX/` contains:
- ✅ Source code
- 📄 Problem statements or lab briefs
- 🧪 Output screenshots or result logs (if applicable)
- 📝 Explanations or summary reports

---

## 🧠 About the Project – ACCESS-RIDE

**ACCESS-RIDE** is a smart transportation scheduler designed to assist **elderly individuals and people with accessibility needs** in booking and managing transportation with local volunteers or service providers. It provides a user-friendly platform with real-time ride scheduling, intelligent routing, and data visualization.

### Key Features:
- 🧑‍💻 User and driver registration and profiles  
- 🚗 Ride request and matching based on time, location, and accessibility  
- 📍 Route optimization with Google Maps API and Dijkstra/A*  
- 📊 Ride analytics via Matplotlib  
- 🖥️ Cross-platform desktop UI using Flet  
- 🗂️ Backend built with FastAPI and MongoDB  

---

## 🛠️ Technologies Used

- **Python 3**
- **Flet** – Desktop frontend framework
- **FastAPI** – Backend API service
- **MongoDB** – NoSQL database
- **Google Maps API** – Routing and geolocation
- **Matplotlib** – Data visualization

---
## Intructions
1. Install all the required dependencies from the requirements.txt file: pip install -r requirements.txt
2. Configure MongoDB
Ensure MongoDB is running on your machine. The app will default to connecting to localhost:27017, but you can modify the connection string in the db.py file if needed. If MongoDB is not installed, you can follow the MongoDB installation guide for your operating system.
3. Configure MongoDB
Ensure MongoDB is running on your machine. The app will default to connecting to localhost:27017, but you can modify the connection string in the db.py file if needed. If MongoDB is not installed, you can follow the MongoDB installation guide for your operating system.
4. Google Maps API Key
If you'd like to use the Google Maps API for route optimization, you'll need an API key. You can obtain it from Google Cloud Console. Once you have the key, you'll need to integrate it into the app. You can update the ride_scheduler.py file where the route calculation is handled.
5. Run the FastAPI App
To run the FastAPI app, use uvicorn. In your terminal, navigate to the root directory of the project and run: uvicorn main:app --reload
6. Running the Desktop Application (Flet UI)
For the desktop app, you can run it separately from the backend if needed. Here’s how you can start the Flet UI app: python flet_app.py

---

## API Endpoints
Here is a list of the core API endpoints available:

POST /register_user: Registers a new user.

POST /register_driver: Registers a new driver.

POST /login: Logs a user in and returns a JWT access token.

POST /book_ride: Books a ride for a user with a specific driver.

PUT /update_ride_status/{ride_id}: Updates the status of a ride (e.g., Completed, Cancelled).

GET /ride_history/{user_id}: Retrieves the ride history for a user.

GET /calculate_route: Calculates the best route between pickup and dropoff locations.

---

## Data Model
Data Model
The application uses MongoDB for data storage, with the following collections:

  Users: Stores user details like email, password (hashed), etc.

  Drivers: Stores driver details like availability, vehicle info, etc.

  Rides: Stores ride details like pickup/dropoff location, status, and assigned driver.

---

## 👥 Team Members 

- **William Sebastian G. Chuawee**
- **Dustin Dwainne M. Fernandez** 
- **Aelissa Leona P. Pascual** 

