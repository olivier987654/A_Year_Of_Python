# Python Script to get data from Spotify API

import requests
import json
import pandas as pd
import numpy as np
import time
import datetime
import os
import sys
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

# Get the current working directory

cwd = os.getcwd()

# Get the current date

today = datetime.date.today()

# Get the current time

now = datetime.datetime.now()

# URL for the API call

url = "https://api.spotify.com/v1/me/top/tracks"

# Headers for the API call

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

# Parameters for the API call

params = (
    ('time_range', 'short_term'),
    ('limit', '50'),
    ('offset', '0'),
)

# Get the access token from the environment variable

access_token = os.environ.get('SPOTIFY_ACCESS_TOKEN')

# Set the access token in the headers

headers['Authorization'] = 'Bearer ' + access_token

# Make the API call

response = requests.get(url, headers=headers, params=params)

# Get the response in JSON format

response_json = response.json()

# Get the items from the response

items = response_json['items']

# Create a list to store the track names

track_names = []

# Create a list to store the track artists

track_artists = []

# Create a list to store the track ids

track_ids = []

