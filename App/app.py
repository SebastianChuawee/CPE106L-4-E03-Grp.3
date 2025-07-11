# app.py

import flet as ft
from auth_logic import authenticate, register_user

def main(page: ft.Page):
    page.title = "Accessible Transportation - Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    username = ft.TextField(label="Username", width=300)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)
    message = ft.Text(color="red")

    def login_clicked(e):
        if authenticate(username.value, password.value):
            message.value = f"✅ Welcome, {username.value}!"
            message.color = "green"
        else:
            message.value = "❌ Invalid username or password."
            message.color = "red"
        page.update()

    def register_clicked(e):
        if register_user(username.value, password.value):
            message.value = "✅ Registration successful."
            message.color = "green"
        else:
            message.value = "⚠️ Username already exists."
            message.color = "orange"
        page.update()

    page.add(
        ft.Column([
            ft.Text("Login to Your Scheduler", size=20, weight=ft.FontWeight.BOLD),
            username,
            password,
            ft.Row([
                ft.ElevatedButton("Login", on_click=login_clicked),
                ft.OutlinedButton("Register", on_click=register_clicked),
            ]),
            message
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
