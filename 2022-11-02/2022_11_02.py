## Search NBA players stats by name

import requests # This allows us to make requests to the web

# Get the player name

player_name = input("Enter the player name: ") # Asks the user to enter the player name

# Get the player stats

response = requests.get("https://www.balldontlie.io/api/v1/players?search=" + player_name) # This gets the player stats from the API

# Condition to check if the player exists

if response.json()["meta"]["total_count"] == 0: # This checks if the player exists

    print("Player not found")

else:

    # Get the player id

    player_id = response.json()["data"][0]["id"]

    # Get the player stats

    response = requests.get("https://www.balldontlie.io/api/v1/season_averages?season=2021&player_ids[]=" + str(player_id))

    # Get the player stats

    player_stats = response.json()["data"][0]

    # Print the player stats

    print("Player: " + player_name)

    print("Points: " + str(player_stats))





