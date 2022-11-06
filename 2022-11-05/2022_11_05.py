## Get the price of a specific stock with ticker symbol input

import requests # This allows us to make requests to the web

# Get the stock ticker symbol

stock_ticker = input("Enter the stock ticker symbol: ") # Asks the user to enter the stock ticker symbol

# Get the stock price

response = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + stock_ticker + "&apikey=YOUR_API_KEY") # This gets the stock price from the API

# Condition to check if the stock exists

if response.json()["Global Quote"] == {}: # This checks if the stock exists
    print ("Stock not found")
else:
    # Get the stock price
    stock_price = response.json()["Global Quote"]["05. price"]
    # Print the stock price
    print("The price of " + stock_ticker + " is $" + stock_price)

