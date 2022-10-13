# Python API for the OpenWeatherMap API

from datetime import date
import requests
import json
import sys

# Define your API key
API_KEY = "YOUR_API_KEY"

# Define the Base URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Define the city
CITY = "Montreal"

# Define the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

# Send the request
response = requests.get(URL)

# Check the status code
if response.status_code == 200:
    # Get the data
    data = response.json()
    # Get the main data
    main = data['main']
    # Get the temperature
    temperature = main['temperature']
    # Get the humidity
    humidity = main['humidity']
    # Get the pressure
    pressure = main['pressure']
    # Get the weather
    weather = data['weather']
    # Get the description
    description = weather[0]['description']
    # Print the data
    print("Temperature: " + str(temperature))
    print("Humidity: " + str(humidity))
    print("Pressure: " + str(pressure))
    print("Description: " + str(description))

else:

    # Print the error
    print("Error in the HTTP request, make sure you have the right API key")






