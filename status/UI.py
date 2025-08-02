import flet as ft
import requests
import json
import asyncio

# Global variables
user_id = "user123"  # Example user ID

def user_dashboard(page):
    page.title = "Accessible Transportation - User Dashboard"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Login Form
    email_input = ft.TextField(label="Email", autofocus=True)
    password_input = ft.TextField(label="Password", password=True)

    login_button = ft.ElevatedButton("Login", on_click=lambda e: login_user(e, email_input, password_input, page))
    
    # Ride Booking Form
    ride_form = ft.Column(
        controls=[
            ft.Text("Book a Ride"),
            ft.TextField(label="Pick-Up Location"),
            ft.TextField(label="Drop-Off Location"),
            ft.DatePicker(label="Preferred Pickup Time"),
            ft.ElevatedButton("Book Ride", on_click=lambda e: book_ride(e, page))
        ]
    )

    # Live Ride Status
    live_status_text = ft.Text("Waiting for ride status updates...")

    def update_ride_status():
        # Fetch the latest ride status (simulate real-time update)
        response = requests.get(f"http://localhost:8000/get_ride_status/{user_id}")
        if response.status_code == 200:
            ride_status = response.json()
            live_status_text.value = f"Current Status: {ride_status['status']}"
        else:
            live_status_text.value = "Failed to fetch status."
        page.update()

    # Timer to refresh the ride status every 5 seconds
    page.add(live_status_text)
    page.add(email_input, password_input, login_button, ride_form)
    
    page.timer = ft.Timer(5000, update_ride_status)

def login_user(event, email_input, password_input, page):
    email = email_input.value
    password = password_input.value
    payload = {"email": email, "password": password}

    response = requests.post("http://localhost:8000/login", json=payload)
    if response.status_code == 200:
        page.add(ft.Text("Login Successful!"))
        show_ride_options(page)
    else:
        page.add(ft.Text("Invalid credentials, please try again"))

def show_ride_options(page):
    # Placeholder function to show available ride options
    page.add(ft.Text("Available Rides"))
    # Here, you would pull real-time data and display available rides

def book_ride(event, page):
    # Simulate booking a ride
    page.add(ft.Text("Ride Booked!"))
    # Send request to backend to book the ride

ft.app(target=user_dashboard)
