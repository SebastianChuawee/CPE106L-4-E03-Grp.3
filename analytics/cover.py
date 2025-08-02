import folium
from folium.plugins import HeatMap

def plot_coverage_heatmap():
    # Get ride data
    ride_data = get_ride_data()

    # Extract user pickup locations (lat, lon)
    locations = [ride["user_location"] for ride in ride_data]

    # Create a folium map centered around the mean location
    map_center = [np.mean([loc[0] for loc in locations]), np.mean([loc[1] for loc in locations])]
    ride_map = folium.Map(location=map_center, zoom_start=12)

    # Add heatmap to the map
    HeatMap(locations).add_to(ride_map)

    # Save the map to an HTML file
    ride_map.save("ride_coverage_heatmap.html")
    print("Coverage heatmap saved as ride_coverage_heatmap.html")
