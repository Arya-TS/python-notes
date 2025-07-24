'''
The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

Create a weight conversion program that:

Asks the user what their Earth weight is (as a float).
Asks the user for a planet number (as an int).
Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

To calculate the user's weight:

destination weight=Earth weight × relative gravity
Number	Planet	Relative Gravity
1	Mercury	0.38
2	Venus	0.91
3	Mars	0.38
4	Jupiter	2.53
5	Saturn	1.07
6	Uranus	0.89
7	Neptune	1.14
If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.
'''

# Write code below 💖

earth_weight = float(input("Enter earth weight: "))
num = int(input("Enter planet number: "))
if num == 1:
    destination_weight = earth_weight*0.38
elif num == 2:
    destination_weight = earth_weight*0.91
elif num == 3:
    destination_weight = earth_weight*0.38
elif num == 4:
    destination_weight = earth_weight*2.53
elif num == 5:
    destination_weight = earth_weight*1.07
elif num == 6:
    destination_weight = earth_weight*0.89
elif num == 7:
    destination_weight = earth_weight*1.14
else:
    print("Invalid planet number")
print(f"user weight = {destination_weight}")
