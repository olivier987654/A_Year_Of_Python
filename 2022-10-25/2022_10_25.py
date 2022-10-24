# Python Script to get ip address of a website 

import socket

def get_ip_address(url): # This line is defining a function called get_ip_address
    try:
        ip = socket.gethostbyname(url)
        print(f"IP address of {url} is {ip}")
    except:
        print("Unable to get IP address")

if __name__ == "__main__":
    url = input("Enter a website url: ")
    get_ip_address(url)

