#-------------------------------------------------------------------------
# Name:       Login
# Purpose:    Checks if username and password are correct
# Author:     Chen. C
# Created:    03/05/2024
#-------------------------------------------------------------------------

# Initialize correct username and password
correct_username = "StAugustineCHS"
correct_password = "Coding123!"

# Get username and password from user
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

while correct_username != entered_username or correct_password != entered_password:
  # When both username and password are incorrect
  if correct_username != entered_username and correct_password != entered_password:
    print("Username and password incorrect.\n")

  # When only username is incorrect
  elif correct_username != entered_username:
    print("Username incorrect.\n")
  
  # When only password is incorrect
  elif correct_password != entered_password:
    print("Password incorrect.\n")

  # Prompt user again in all cases
  entered_username = input("Enter your username: ")
  entered_password = input("Enter your password: ")

# Output message when username and password are correct
print("Welcome!")