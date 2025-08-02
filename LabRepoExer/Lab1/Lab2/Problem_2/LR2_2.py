
def main():
    """
    Main function to run the line navigation program.
    """
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as f:
            
            lines = f.readlines()
            
            lines = [line.strip() for line in lines]
            num_lines = len(lines)
            
            while True:
                print(f"\nThe file has {num_lines} lines.")
                
                try:
                    
                    line_number_input = input("Enter a line number (1-{} or 0 to quit): ".format(num_lines))
                    line_number = int(line_number_input)
                    
                    
                    if line_number == 0:
                        print("Exiting program. Goodbye!")
                        break
                    
                    
                    if 1 <= line_number <= num_lines:
                        
                        print(f"Line {line_number}: {lines[line_number - 1]}")
                    else:
                        print("Error: Invalid line number. Please enter a number between 1 and {}.".format(num_lines))
                
                except ValueError:
                    
                    print("Error: Invalid input. Please enter a number.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    
if __name__ == "__main__":
    main()

