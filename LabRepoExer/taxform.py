
def main():
    print("Welcome to the Tax Calculator")

    # Input from the user
    income = float(input("Enter your taxable income: "))

    # Fixed tax rate (e.g., 20%)
    tax_rate = 0.20

    # Calculate tax
    tax = income * tax_rate

    # Round to 2 decimal places
    tax = round(tax, 2)

    # Display result
    print("The tax is", tax)

if __name__ == "__main__":
    main()
