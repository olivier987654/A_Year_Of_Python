## Extract data from HTML / XML using BeautifulSoup

## This Script allows you to scrape data from a website and print it to the console

import requests
from bs4 import BeautifulSoup

# URL to scrape

url = "https://www.google.com/" # You can change it to the url you want to scrape

# Get the HTML content

html = requests.get(url).content

# Parse the HTML content

soup = BeautifulSoup(html, "html.parser")

# Get the title of the page

title = soup.title.text

# Get the first paragraph

first_paragraph = soup.p.text

# Get all the links in the page

links = [element.get("href") for element in soup.find_all("a")]

# Get all the images in the page

images = [element.get("src") for element in soup.find_all("img")]

# Print the results

print(title)

print(first_paragraph)

print(links)

print(images)



