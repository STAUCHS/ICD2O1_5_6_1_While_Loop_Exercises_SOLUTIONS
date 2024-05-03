#-------------------------------------------------------------------------
# Name:       Sum 1 to N
# Purpose:    Sum all the numbers from 1 to n (given by user)
# Author:     Chen. C
# Created:    03/05/2024
#-------------------------------------------------------------------------

# Get number from user
n = int(input("Enter a number: "))

# Initialize variables
count = 0
sum = 0

# Loop through all numbers from 1 to n
while count <= n:
  sum += count
  count += 1

# Output sum
print(f"The sum of all numbers from 1 to {n} is {sum}")