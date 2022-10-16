# Python Script to download a youtube video

import pytube

# Enter the link of the video you want to download

link = input("Enter the link of the video you want to download: ")

# Creating an object of the YouTube class

yt = pytube.YouTube(link)

# Getting the highest resolution possible

stream = yt.streams.get_highest_resolution()

# Downloading the video

stream.download()

# Successful Download

print("Download completed!!")

# Printing the title of the video

print("Title: ", yt.title)

# Printing the number of views of the video

print("Number of views: ", yt.views)

# Printing the length of the video

print("Length of video: ", yt.length, "seconds")

# Printing the description of the video

print("Description: ", yt.description)