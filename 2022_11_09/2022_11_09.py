## Simple Script that reads the user input and prints an answer

# Get the user input

# Define a varible

my_name = input("What is your name? ")

user_input = input("Enter a number: ") # Asks the user to enter a number

# Condition to check if the user input is a number

if user_input.isdigit(): # This checks if the user input is a number
    print(my_name + "," + " You entered a number")

else:
    print(my_name + "," + " You did not enter a number")




# This script will check if the user input is a number or not.

if user_input == "1":
    print(my_name + "," + " You entered 1")

elif user_input == "2":
    print(my_name + "," + " You entered 2")

elif user_input == "3":
    print(my_name + "," + " You entered 3")

else:
    print(my_name + "," + " You did not enter 1, 2 or 3")
