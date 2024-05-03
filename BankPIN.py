#-------------------------------------------------------------------------
# Name:       Bank PIN
# Purpose:    Validate user's PIN
# Author:     Chen. C
# Created:    03/05/2024
#-------------------------------------------------------------------------

# Output title
print("WELCOME TO STA BANK!")

# Intialize correct PIN
correct_PIN = 3819

# Get PIN from user
entered_PIN = int(input("\nEnter your PIN: "))

# Reprompt user when PINs don't match
while correct_PIN != entered_PIN:
  print("Incorrect PIN. Try again.")
  entered_PIN = int(input("\nEnter your PIN: "))

# Output message when PIN is correct
print("PIN accepted. You may now access your account.")