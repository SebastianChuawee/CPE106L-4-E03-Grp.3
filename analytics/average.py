def plot_avg_wait_time():
    # Get ride data
    ride_data = get_ride_data()

    # Extract wait times for all rides
    wait_times = [ride["wait_time"] for ride in ride_data]

    # Calculate average wait time
    avg_wait_time = np.mean(wait_times)

    # Plotting the average wait time
    plt.figure(figsize=(10, 6))
    plt.hist(wait_times, bins=20, color="g", alpha=0.7, label="Wait Times")
    plt.axvline(avg_wait_time, color='r', linestyle='dashed', linewidth=2, label=f"Avg Wait Time: {avg_wait_time:.2f} mins")
    plt.title("Distribution of Ride Wait Times")
    plt.xlabel("Wait Time (minutes)")
    plt.ylabel("Frequency")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
