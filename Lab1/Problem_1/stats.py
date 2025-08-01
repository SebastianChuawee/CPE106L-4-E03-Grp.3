# stats.py

def mean(numbers):
    """Return the average of the numbers in the list."""
    return sum(numbers) / len(numbers)


def median(numbers):
    """Return the median value of the numbers in the list."""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    middle = n // 2

    if n % 2 == 0:
        # Average of the two middle numbers
        return (sorted_nums[middle - 1] + sorted_nums[middle]) / 2
    else:
        # Middle number
        return sorted_nums[middle]


def mode(numbers):
    """Return the mode (most frequent value) of the numbers in the list."""
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]

    # If all numbers appear only once, there's no mode — return None
    if len(modes) == len(frequency):
        return None
    return modes[0]  # Return the first mode if multiple

# Example usage:
if __name__ == "__main__":
    data = [1, 2, 3, 4, 4, 5]
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))
