'''
# A number is "squared" when it is either multiplied by itself or taken to the second power (e.g., 4² = 4 x 4 = 16).
#
# First, ask the user for an integer with int(input()) and store it in a variable called `number`.
# Then, define a variable `total` with an initial value of 0.
#
# Note: You can pass a string prompt to int(input()).
#
# Next, use a for loop and the range() function to calculate the total of the squares 
# of all integers from 1 to that number.
#
# Last, print the output as an integer value.
#
# For example, if number is 5, the total should be 55 because:
# 1² + 2² + 3² + 4² + 5² = 1 + 4 + 9 + 16 + 25 = 55

'''

# Write code below 💖
number = int(input("Enter an integer: "))
total = 0
for i in range(1, number+1):
    total += i**2
print(total)
