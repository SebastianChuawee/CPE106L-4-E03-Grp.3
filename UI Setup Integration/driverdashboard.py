import flet as ft
import requests

def driver_dashboard(page):
    page.title = "Accessible Transportation - Driver Dashboard"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Login Form
    email_input = ft.TextField(label="Email", autofocus=True)
    password_input = ft.TextField(label="Password", password=True)

    login_button = ft.ElevatedButton("Login", on_click=lambda e: login_driver(e, email_input, password_input, page))

    page.add(
        email_input,
        password_input,
        login_button
    )

def login_driver(event, email_input, password_input, page):
    email = email_input.value
    password = password_input.value
    payload = {"email": email, "password": password}

    # Send the login request to the FastAPI backend
    response = requests.post("http://localhost:8000/login", json=payload)
    if response.status_code == 200:
        page.add(ft.Text("Login Successful!"))
        # Proceed to show assigned rides for driver
        show_assigned_rides(page)
    else:
        page.add(ft.Text("Invalid credentials, please try again"))

def show_assigned_rides(page):
    # Fetch assigned rides from the backend
    response = requests.get("http://localhost:8000/assigned_rides")
    if response.status_code == 200:
        rides = response.json()
        for ride in rides:
            ride_info = f"Ride ID: {ride['ride_id']}, Status: {ride['status']}"
            page.add(ft.Text(ride_info))
            # Add an "Update Status" button for each ride
            update_button = ft.ElevatedButton("Update Status", on_click=lambda e: update_ride_status(e, ride['ride_id'], page))
            page.add(update_button)

def update_ride_status(event, ride_id, page):
    # Send a request to update the ride status
    payload = {"ride_id": ride_id, "status": "In Progress"}
    response = requests.put(f"http://localhost:8000/update_ride_status/{ride_id}", json=payload)
    if response.status_code == 200:
        page.add(ft.Text(f"Ride {ride_id} status updated to In Progress"))
    else:
        page.add(ft.Text("Failed to update ride status"))

ft.app(target=driver_dashboard)
