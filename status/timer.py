def driver_dashboard(page):
    page.title = "Accessible Transportation - Driver Dashboard"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Login Form
    email_input = ft.TextField(label="Email", autofocus=True)
    password_input = ft.TextField(label="Password", password=True)

    login_button = ft.ElevatedButton("Login", on_click=lambda e: login_driver(e, email_input, password_input, page))
    
    # Live Ride Status for Drivers
    driver_live_status_text = ft.Text("Waiting for ride status updates...")

    def update_driver_ride_status():
        # Fetch the latest ride status for the driver (simulate real-time update)
        response = requests.get(f"http://localhost:8000/get_driver_ride_status/{user_id}")
        if response.status_code == 200:
            ride_status = response.json()
            driver_live_status_text.value = f"Current Ride Status: {ride_status['status']}"
        else:
            driver_live_status_text.value = "Failed to fetch status."
        page.update()

    # Timer to refresh ride status every 5 seconds
    page.add(driver_live_status_text)
    page.add(email_input, password_input, login_button)
    
    page.timer = ft.Timer(5000, update_driver_ride_status)
