import flet as ft
import requests

def user_dashboard(page):
    page.title = "Accessible Transportation - User Dashboard"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Login Form
    email_input = ft.TextField(label="Email", autofocus=True)
    password_input = ft.TextField(label="Password", password=True)

    login_button = ft.ElevatedButton("Login", on_click=lambda e: login_user(e, email_input, password_input, page))
    
    # Ride booking form
    ride_form = ft.Column(
        controls=[
            ft.Text("Book a Ride"),
            ft.TextField(label="Pick-Up Location"),
            ft.TextField(label="Drop-Off Location"),
            ft.DatePicker(label="Preferred Pickup Time"),
            ft.ElevatedButton("Book Ride", on_click=lambda e: book_ride(e, page))
        ]
    )

    # Cancel ride form
    cancel_ride_form = ft.Column(
        controls=[
            ft.Text("Cancel Ride"),
            ft.TextField(label="Ride ID"),
            ft.ElevatedButton("Cancel Ride", on_click=lambda e: cancel_ride(e, page))
        ]
    )

    page.add(
        email_input,
        password_input,
        login_button,
        ride_form,
        cancel_ride_form
    )

def login_user(event, email_input, password_input, page):
    email = email_input.value
    password = password_input.value
    payload = {"email": email, "password": password}

    # Send the login request to the FastAPI backend
    response = requests.post("http://localhost:8000/login", json=payload)
    if response.status_code == 200:
        page.add(ft.Text("Login Successful!"))
        # Proceed to the ride booking part after login
        show_ride_options(page)
    else:
        page.add(ft.Text("Invalid credentials, please try again"))

def show_ride_options(page):
    # Placeholder function for now to show available ride options
    page.add(ft.Text("Available Rides"))
    # Add ride options UI

def book_ride(event, page):
    # Send ride booking request to FastAPI backend
    page.add(ft.Text("Ride Booked!"))
    # Integrate ride booking API later

def cancel_ride(event, page):
    # Send ride cancel request to FastAPI backend
    page.add(ft.Text("Ride Canceled!"))
    # Integrate cancel ride API later

ft.app(target=user_dashboard)
