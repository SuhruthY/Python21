import random
import math

## Getting range from user inputs
try:
    low = int(input("Enter lower boundary:"))
    upp = int(input("Enter upper boundary:"))
except:
    low, upp = 1, 100
#print(low, upp)

## Generating a Random Number
num = random.randint(low, upp)
num_of_chances = round(math.log(upp - low + 1,2))
print("You have only ", num_of_chances, " chances to win the GAME")



""" Main Program """

chances_so_far = 0 # initialializing var

# Main GAME loop
while chances_so_far < num_of_chances:
    chances_so_far += 1
    guess = int(input("Guess a number :- "))

    if num == guess:
        print("Congratualtions\nyou did it in ", chances_so_far," tries.\n\n","   ---You won---\n")
        break
    elif num > guess:
        print("Your guess is too small")
    elif num < guess:
        print("Your guess is too big")

if chances_so_far >= num_of_chances:
    print("\nThe number is {}".format(num))
    print("\nBetter Luck Next Time!")
