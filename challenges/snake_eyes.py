'''
Thank you codedex!
Suppose we have a pair of dice. 🎲 🎲

In dice games, "snake eyes" means rolling two 1s. Why is it called that? Because two small dots look like a pair of snake eyes. 🐍👀

It’s the lowest possible roll (1 + 1 = 2) and is seen as bad luck. 😅

Let's keep rerolling two dice until we get snake eyes.

Nope
Nope
Nope
Nope
Snake eyes!

First, use the random module to “roll” the two dice.

Each die (die1 and die2) has an integer value from 1 to 6.

Store the sum of the two random values in a new total variable.

Until the total is 2, use a while loop to keep "rerolling" the dice and print out a simple 'Nope'.

'''

# Write code below 💖
import random
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2
while total != 2:
    print("Nope")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
print("Snake eyes!")
