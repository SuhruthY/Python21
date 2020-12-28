from random import randint

def get_choice_name(choice):
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
    return choice_name

def get_winner():
    # condition for winning
    if ((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
        print("Paper wins => ", end="")
        result = "Paper"

    elif ((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end="")
        result = "Rock"
    else:
        print("Scissor wins =>", end="")
        result = "Scissor"

    # Printing either user or computer wins
    if result == user_choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

print( "\n","\t\t\t\t\tWElCOME TO\n---------- TINKU'S Rock-Paper-Scissor ----------\n")

print(f"""Winning Rules of the Rock-Paper-Scissor game as follows:
        Rock vs Paper -> Paper wins      
        Rock vs Scissor -> Rock wins      
        Paper vs Scissor -> Scissor wins
-------------------------------------------------------------""")

print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")

game_still_going = True
while game_still_going:
    ## user choice
    # take the input from user
    choice = input("User turn: ")
    # looping until user enter invalid input )
    while choice not in ["1", "2", "3"]:
        choice = input("enter valid input: ")
    choice = int(choice)
    # get corresponding choice name
    user_choice_name = get_choice_name(choice)
    # print user choice
    print(f"\nUser choice is: {user_choice_name}\nNow its computer turn.......")


    ## computer choice
    # choosing a random choice
    comp_choice = randint(1, 3)
    # making sure computer choosing different from user
    while comp_choice == choice:
            comp_choice = randint(1, 3)
    # get corresponding choice name
    comp_choice_name = get_choice_name(comp_choice)
    print(f"\nComputer choice is: {comp_choice_name}\n\n{user_choice_name} VS {comp_choice_name}")

    print(choice, user_choice_name, comp_choice, comp_choice_name)

    ## select winner
    get_winner()

    ## wanna play again
    ask = input("\nwanna play again?(Y/N):")
    if ask not in ["Y", "y", "N", "n"]:
        game_still_going = False
    else:
        continue
    print("\n")
