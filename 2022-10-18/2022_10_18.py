# Detect DDos attack using scapy and python3

from scapy.all import *
import time
import sys
import os

# Global variables

# The number of packets to sniff

packet_count = 100

# The time to wait between packets

inter_packet_time = 0.1

# The time to wait between printing output

inter_print_time = 1

# The number of packets that must be seen in a given time period to trigger an alert

threshold = 100

# The time period over which the threshold is applied

threshold_time = 10

# The IP address to monitor (Input from user)

monitor_ip = " 0.0.0.0 "

# The IP address to block by default (Input from user)

block_ip = "0.0.0.0"