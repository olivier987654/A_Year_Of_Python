# Discord Bot using python3 to send command to the Pokecatcher channel.


import random
import discord
from discord.ext import tasks

# Init the discord client
discord_client = discord.Client()

channel_id = 000000000000000000 # Replace with your channel ID

# Set the channel object using our channel ID number
channel = discord_client.get_channel(channel_id)

# List we will use these in the example to send random messages to the server
messages = [ "INPUT THE TEXT OR COMMAND YOU WANT TO SEND HERE" ]

# Single message to get sent to the server string
single_message = "This will send over and over if multi_message = False."

# We will use this boolean to determine if we are just sending message string or a random one from messages list
multi_message = False
        
# Create a loop task for every 60 minutes [1 hour]
@tasks.loop(minutes = 60) # You can change this to seconds, hours, days, etc.
async def send_message():
    # Call channel so we can modify it's value
    global channel
    # Make sure channel isn't null
    if channel == None:
        channel = discord_client.get_channel(channel_id)
    # Wait for the discord bot to load before we start posting
    await discord_client.wait_until_ready()
    # Check to see if we are going to be sending different messages every hour or not
    if multi_message:
        # Print to output
        print("Posted random message.")
        # Send message to Discord channel
        await channel.send(f"{random.choice(messages)}")
    else:
        print("Posted single message")
        await channel.send(f"{single_message}")

# On bot ready
@discord_client.event
async def on_ready():
    # Check to see if we are going to be sending different messages every hour or not
    if multi_message:
        print("* Sending random messages to the channel...")
    else:
        print("* Sending single message to the channel...")

    # Start the message sending loop
    send_message.start()

    # Finished setting up
    print("The Bot ready.")

# Launch the Discord bot
print("+ Loading Discord message posting bot...")
discord_client.run("INPUT YOUR BOT TOKEN HERE")