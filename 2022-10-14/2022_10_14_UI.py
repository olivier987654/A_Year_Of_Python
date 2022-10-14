# UI for the dice roller

import random


print("Welcome to the dice roller my friend!")

# Ask the user for the number of sides

dice_sides = input("How many sides should the dice have? ")

# Roll the dice

dice_roll = random.randint(1, int(dice_sides))

# Print the result

print("You rolled a " + str(dice_roll))

# Ask the user if they want to roll again

roll_again = input("Do you want to roll again? (y/n) ")

# Check if the user wants to roll again

if roll_again == "y":

    # Roll the dice again

    dice_roll = random.randint(1, int(dice_sides))

    # Print the result

    print("You rolled a " + str(dice_roll))

# Loop until the user says no

while roll_again == "y":

    # Ask the user if they want to roll again

    roll_again = input("Do you want to roll again? (y/n) ")

    # Check if the user wants to roll again

    if roll_again == "y":

        # Roll the dice again

        dice_roll = random.randint(1, int(dice_sides))

        # Print the result

        print("You rolled a " + str(dice_roll))

    else:

        # Print a message

        print("Thanks for playing!")




