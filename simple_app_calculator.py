# This program will ask the user to pick which mathematical operations (addition, subtraction, multiplication, and division) to perform then ask for two numbers.

# Start of program
# Ask the user which mathematical operation to perform
while True:
    try:
        operation = input("What mathematical operation would you like to perform? Please enter the corresponding number of the operation to proceed.\n1 Addition\n2 Subtraction\n3 Multiplication\n4 Division\n")
        if operation not in ['1','2','3','4']:
            print("Invalid input. Please enter the number before the operation.")
            continue
# Ask the user to enter the first number
        first_number = float(input("Enter the first number: "))
# Ask the user to enter the second number
        second_number = float(input("Enter the second number: "))
# Perform the operation
        if operation == "1":
            sum = first_number + second_number
# Print the result 
            print("The sum is",sum)
        elif operation == "2":
            difference = first_number - second_number
# Print the result 
            print("The difference is",difference)
        elif operation == "3":
            product = first_number * second_number
# Print the result 
            print("The product is",product)
        else:
            if operation == "4":
                quotient = first_number / second_number
# Print the result 
                print("The quotient is",quotient)
# Print an error message when there is an error
    except ZeroDivisionError:
        print("Division by zero error.")
    except ValueError as e:
        print("Error: ",e)
    except:
        print("Unknown Error.")
# Ask the user if they want to try again
    try:
        try_again = input("Do you want to try again? (y/n): ")
        if try_again.lower() == "y":
            continue
        elif try_again.lower() == "n":
            print("Thank you!")
            break
        else:
            print('The program identified that you did not enter "y/n". The program will close now. Thank you!')
            break
# Print an error message when there is an error
    except:
        print("Unknown Error")

# End of program