#-------------------------------------------------------------------------
# Name:       Dice Doubles
# Purpose:    Simulates dices rolls until a double appears
# Author:     Chen. C
# Created:    03/05/2024
#-------------------------------------------------------------------------

import random

# Generate dice rolls and sum them
roll1 = random.randrange(1, 7)
roll2 = random.randrange(1, 7)
sum = roll1 + roll2

# Output title
print("HERE COMES THE DICE!\n")

# Checks if the first roll is a double
if roll1 == roll2:
  print(f"Roll #1: {roll1}")
  print(f"Roll #2: {roll2}")
  print(f"The total is {sum}!\n")

# Roll until double is reached
while roll1 != roll2:
  roll1 = random.randrange(1, 7)
  roll2 = random.randrange(1, 7)
  sum = roll1 + roll2
  print(f"Roll #1: {roll1}")
  print(f"Roll #2: {roll2}")
  print(f"The total is {sum}!\n")