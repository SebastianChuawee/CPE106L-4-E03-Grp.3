def plot_ride_frequency():
    # Get ride data from MongoDB
    ride_data = get_ride_data()

    # Extract the pickup dates for each ride
    pickup_dates = [ride["pickup_time"].date() for ride in ride_data]

    # Count ride occurrences per day
    unique_dates = sorted(set(pickup_dates))
    ride_count_per_day = [pickup_dates.count(date) for date in unique_dates]

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(unique_dates, ride_count_per_day, marker="o", linestyle="-", color="b", label="Rides")
    plt.title("Ride Frequency Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Rides")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
