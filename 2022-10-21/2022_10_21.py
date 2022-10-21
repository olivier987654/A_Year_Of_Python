# Python Script to monitor network with UI and log to file

import os
import time
import datetime
import subprocess
import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title("Network Monitor")
window.geometry("500x500")

# Create a label
label = tk.Label(text="Network Monitor")
label.pack()

# Create a button
button = tk.Button(text="Start", width=25, command=window.destroy)
button.pack()

# Monitor network
def monitor_network():
    # Get current time
    now = datetime.datetime.now()
    # Create a file name with current time
    file_name = now.strftime("%Y-%m-%d-%H-%M-%S") + ".txt"
    # Create a file with current time
    file = open(file_name, "w")
    # Write the header to the file
    file.write("Time,Status,IP Address,MAC Address")
    
    # Loop forever
    while True:
        # Get current time
        now = datetime.datetime.now()
        # Get current time in string format
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        # Ping Google
        response = os.system("ping -n 1")
