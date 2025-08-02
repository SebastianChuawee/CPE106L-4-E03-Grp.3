# test_flet_ui.py
import pytest
import flet as ft
from flet.testing import AppRunner

def test_user_login():
    with AppRunner(target=user_dashboard) as app:
        app.page.get_control("email_input").value = "test@example.com"
        app.page.get_control("password_input").value = "password"
        app.page.get_control("login_button").click()

        # Simulate backend interaction, verify success
        assert "Login Successful!" in app.page.controls

def test_book_ride():
    with AppRunner(target=user_dashboard) as app:
        app.page.get_control("pickup_location").value = "Bangalore"
        app.page.get_control("dropoff_location").value = "Mysore"
        app.page.get_control("ride_button").click()

        # Check if ride booking was successful
        assert "Ride Booked!" in app.page.controls
