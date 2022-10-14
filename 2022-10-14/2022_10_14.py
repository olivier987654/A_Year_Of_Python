## Small script to roll a dice and print the result

import random

# Define the number of sides
dice_sides = 12

# Roll the dice

dice_roll = random.randint(1, dice_sides)

# Print the result

print("You rolled a " + str(dice_roll))
