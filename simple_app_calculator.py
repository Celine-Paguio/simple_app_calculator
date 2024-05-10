# This program will ask the user to pick which mathematical operations (addition, subtraction, multiplication, and division) to perform then ask for two numbers.

# Start of program
# Ask the user which mathematical operation to perform
while True:
    try:
        operation = input("What mathematical operation would you like to perform? Please enter the corresponding number of the operation to proceed.\n1 Addition\n2 Subtraction\n3 Multiplication\n4 Division\n")
        if operation not in ['1','2','3','4']:
            print("Invalid input. Please enter the number before the operation.")
            continue
    except:
        print("Unknown Error.")
# Ask the user to enter the first number
# Ask the user to enter the second number
# Perform the operation
# Print the result
# Print an error message when there is an error
# Ask the user if they want to try again