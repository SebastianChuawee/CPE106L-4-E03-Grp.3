import requests

# Function to get the route from Google Maps API
def get_route_from_google_maps(start_location, end_location, api_key):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start_location}&destination={end_location}&key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        directions = response.json()
        if directions["status"] == "OK":
            route = directions["routes"][0]["legs"][0]
            distance = route["distance"]["text"]
            duration = route["duration"]["text"]
            return distance, duration
    return None, None

