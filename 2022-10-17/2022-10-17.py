# Python Automation Script to create a new folder

import os
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Create a new folder with the current date and time

os.mkdir(now.strftime("%Y-%m-%d"))

# Print the current date and time
print("Current date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# Select the path where you want to create the folder

os.chdir("COPY THE PATH OF THE FOLDER")

# Print the new folder name

print(os.getcwd())
