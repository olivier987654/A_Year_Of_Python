import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Olivier Port Scanner") # This allow us to print the banner in ASCII format
print(ascii_banner)
# Defining a target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate a host name to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")

    # Add a pretty banner
    print ("-" * 50)
    print ("Scanning target " + target)
    print ("Time started: " + str(datetime.now()))
    print ("-" * 50)

    try:
        for port in range(50,85):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port)) # Returns an error indicator
            print("Checking port {}".format(port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()

    # These commands are exception handlers for the script

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()