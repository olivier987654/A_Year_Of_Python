# Python Script to have Crypto prices in the terminal

# You can change the currency by changing the vs_currencies=usd to vs_currencies=eur etc.

import requests
import json
import time

# Get the current price of Bitcoin
def get_btc_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    response_json = response.json()
    btc_price = response_json["bitcoin"]["usd"]
    return btc_price

# Get the current price of Ethereum
def get_eth_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
    response_json = response.json()
    eth_price = response_json["ethereum"]["usd"]
    return eth_price

# Get the current price of Dogecoin
def get_doge_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd")
    response_json = response.json()
    doge_price = response_json["dogecoin"]["usd"]
    return doge_price

# Get the current price of Solana
def get_sol_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd")
    response_json = response.json()
    sol_price = response_json["solana"]["usd"]
    return sol_price

# Get the current price of Cardano
def get_ada_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd")
    response_json = response.json()
    ada_price = response_json["cardano"]["usd"]
    return ada_price

# Get the current price of Polkadot
def get_dot_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=polkadot&vs_currencies=usd")
    response_json = response.json()
    dot_price = response_json["polkadot"]["usd"]
    return dot_price

# Print the prices
def print_prices():
    print("Bitcoin: $" + str(get_btc_price()))
    print("Ethereum: $" + str(get_eth_price()))
    print("Dogecoin: $" + str(get_doge_price()))
    print("Solana: $" + str(get_sol_price()))
    print("Cardano: $" + str(get_ada_price()))
    print("Polkadot: $" + str(get_dot_price()))

# Run the program
while True:
    print_prices()
    time.sleep(60) # You can change the time to whatever you want
