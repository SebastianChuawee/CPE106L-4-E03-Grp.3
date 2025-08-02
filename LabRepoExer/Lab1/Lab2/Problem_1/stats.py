# stats.py

"""
Module: stats
A set of functions that compute the mean, median, and mode of a set of numbers.
"""

def mean(numbers):
    """
    Computes the mean (average) of a list of numbers.
    Returns 0 if the list is empty.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """
    Computes the median of a list of numbers.
    Returns 0 if the list is empty.
    """
    if not numbers:
        return 0
    
    # Sort the list and print the number at its midpoint
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def mode(numbers):
    """
    Computes the mode of a list of numbers.
    Returns 0 if the list is empty.
    """
    if not numbers:
        return 0
    
    # Obtain the set of unique numbers and their
    # frequencies, saving these associations in
    # a dictionary
    theDictionary = {}
    for number in numbers:
        count = theDictionary.get(number, None)
        if count == None:
            # number entered for the first time
            theDictionary[number] = 1
        else:
            # number already seen, increment its number
            theDictionary[number] = count + 1

    # Find the mode by obtaining the maximum value
    # in the dictionary and determining its key
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            return key
            
def main():
    """
    Tests the statistical functions with a sample list.
    """
    test_list_odd = [1, 2, 3, 4, 5, 5]
    test_list_even = [1, 2, 2, 3, 4, 5]
    test_list_empty = []

    print("--- Testing with list:", test_list_odd, "---")
    print("Mean:", mean(test_list_odd))
    print("Median:", median(test_list_odd))
    print("Mode:", mode(test_list_odd))
    print("\n--- Testing with list:", test_list_even, "---")
    print("Mean:", mean(test_list_even))
    print("Median:", median(test_list_even))
    print("Mode:", mode(test_list_even))
    print("\n--- Testing with empty list ---")
    print("Mean:", mean(test_list_empty))
    print("Median:", median(test_list_empty))
    print("Mode:", mode(test_list_empty))
    
if __name__ == "__main__":
    main()