import random
import math

print("\n---Welcome to NUMBER GUESS---\n")
## Getting range from user inputs
try:
    low = int(input("Enter lower boundary:"))
    upp = int(input("Enter upper boundary:"))
except:
    low, upp = 1, 100

## Generating a Random Number
num = random.randint(low, upp)
num_of_chances = round(math.log(upp - low + 1,2))


# Checking if user input is integer
def is_digit(check_input):
    if check_input.isdigit():
        return True
    return False

""" Main Program """

chances_so_far = 0 # initialializing var
res = None

print("\nNumber will be in the range of {} to {}".format(low, upp))
print("\nYou have only ", num_of_chances, " chances to win the GAME\n")

# Main GAME loop
while chances_so_far < num_of_chances:
    chances_so_far += 1

    guess = input("Guess a number :- ")
    chk = is_digit(guess)

    while chk == False:
        guess = input("Enter the number again: ")
        chk = is_digit(guess)

    guess = int(guess)

    if num == guess:
        print("Congratualtions\nyou did it in ", chances_so_far," tries.\n\n","   ---You won---\n")
        res = "Won"
        break
    elif num > guess:
        print("\nYour guess is too small\n")
    elif num < guess:
        print("\nYour guess is too big\n")

if res == None:
    print("\nThe number is {}".format(num))
    print("\nBetter Luck Next Time!")
