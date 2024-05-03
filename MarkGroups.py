#-------------------------------------------------------------------------
# Name:       Mark Groups
# Purpose:    Categorizes marks into Level 4, 3, 2, 1 or fails
# Author:     Chen. C
# Created:    03/05/2024
#-------------------------------------------------------------------------

# Output title and info
print("*** Mark Groups ***")
print("This program takes a collection of marks and counts how many Level 4s (80 - 100), Level 3s (70 - 79), Level 2s (60 - 69), Level 1s (50 - 59) and fails (0 - 49).\n")

# Get number of marks from
num_of_marks = int(input("How many marks do you want to enter? "))
print("")

# Initialize accumulator variables
count = 0
level4 = 0
level3 = 0
level2 = 0
level1 = 0
fail = 0

while count < num_of_marks:
  # Get mark from user
  mark = float(input("Enter a mark from 0-100: "))

  if mark >= 80 and mark <= 100:
    level4 += 1
  elif mark >= 70:
    level3 += 1
  elif mark >= 60:
    level2 += 1
  elif mark >= 50:
    level1 += 1
  elif mark >= 0:
    fail += 1

  count += 1

# Output summary of marks
print(f"\nThe number of Level 4s: {level4}")
print(f"The number of Level 3s: {level3}")
print(f"The number of Level 2s: {level2}")
print(f"The number of Level 1s: {level1}")
print(f"The number of fails: {fail}")
