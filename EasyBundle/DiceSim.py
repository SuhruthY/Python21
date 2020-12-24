import random

# Global Variables
Dice = [ " ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
loop_var = True

# Display the die
def display_dice():
    print("\n")
    print( "\t" + Dice[0] + Dice[1] + Dice[2] )
    print( "\t" + Dice[3] + Dice[4] + Dice[5] )
    print( "\t" + Dice[6] + Dice[7] + Dice[8] )
    print("\n")

# Refresh for new roll
def refresh():
    global Dice
    Dice = [ " ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

""" --- MAIN PROGRAM --- """
# Simulation
while loop_var == True:
    num = random.randint(1,6)

    if num == 1:
        Dice[4] = "0"
        display_dice()
    elif num == 2:
        Dice[0] = Dice[8] = "0"
        display_dice()
    elif num == 3:
        Dice[3] = Dice[4] = Dice[5] = "0"
        display_dice()
    elif num == 4:
        Dice[0] = Dice[2] = Dice[6] = Dice[8] = "0"
        display_dice()
    elif num == 5:
        Dice[0] = Dice[2] = Dice[4] = Dice[6] = Dice[8] = "0"
        display_dice()
    elif num == 6:
        Dice[0] = Dice[1] = Dice[2] = Dice[6] = Dice[7] = Dice[8] = "0"
        display_dice()

    # user commands and testing
    cmd = input("\nDo you wanna role it again? (Y/N):")
    while cmd not in ["Y","y","N","n"]:
        cmd = input("\nType Either Y or y or N or n only\n\tEnter Again:")
    if cmd in ["Y","y"] :
        refresh()
        loop_var == True
    elif cmd in ["N","n"]:
        print("\n\n\t---END---")
        break
