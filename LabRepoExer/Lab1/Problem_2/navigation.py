def main():
    # Ask user for the filename
    filename = input("Enter the filename: ")

    try:
        # Read all lines from the file into a list
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Remove any trailing newlines
        lines = [line.rstrip('\n') for line in lines]

        # Main loop to navigate through lines
        while True:
            print(f"\nThe file has {len(lines)} lines.")
            line_num = int(input("Enter a line number (0 to quit): "))

            if line_num == 0:
                print("Goodbye!")
                break
            elif 1 <= line_num <= len(lines):
                print(f"Line {line_num}: {lines[line_num - 1]}")
            else:
                print("Invalid line number. Please try again.")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
