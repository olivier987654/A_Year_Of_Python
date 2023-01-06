# First python project of the year.

# Password manger using python

import os
import getpass
import sys


def main():
    print("Welcome to the Password Manager!")
    print("1. Create an account")
    print("2. Log in to your account")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        log_in()
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        main()


def create_account():
    # Prompt the user for their username and password
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    # Check if the username is already taken
    if os.path.exists(f"{username}.txt"):
        print("That username is already taken. Please try again.")
        create_account()
    else:
        # Encrypt the password and save it to a file
        encrypted_password = encrypt(password)
        with open(f"{username}.txt", "w") as f:
            f.write(encrypted_password)
        print("Account created successfully!")
        main()


def log_in():
    # Prompt the user for their username and password
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    # Check if the username and password are correct
    if os.path.exists(f"{username}.txt"):
        with open(f"{username}.txt", "r") as f:
            encrypted_password = f.read()
        if decrypt(encrypted_password) == password:
            print("Logged in successfully!")
            # Show the user their saved passwords
            show_passwords(username)
        else:
            print("Incorrect password. Please try again.")
            log_in()
    else:
        print("No account found with that username. Please try again.")
        log_in()


def show_passwords(username):
    print("Here are your saved passwords:")
    # Read the user's encrypted passwords from their file
    with open(f"{username}.txt", "r") as f:
        encrypted_passwords = f.readlines()
    # Decrypt and print the passwords
    for encrypted_password in encrypted_passwords:
        print(decrypt(encrypted_password))


def encrypt(password):
    # Implement your password encryption logic here
    pass


def decrypt(encrypted_password):
    # Implement your password decryption logic here
    pass


if __name__ == "__main__":
    main()
