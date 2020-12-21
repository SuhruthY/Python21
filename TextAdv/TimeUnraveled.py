# Author : TIm Staler
# Copyright : Comp Sci Central @ compscicentral.com
# Source Code : timstats91 (Github)

from playsound import playsound
import sys
import time
import winsound


# Global Variables
lst_path = ["1","ONE","One","one","2","Two","TWO","two","3","Three",
"THREE","three","4","FOUR","Four","four","5","Five","FIVE","five"]
lst_game = ["yes","Yes","y","Y","no","No","n","N"]
dly = [1, 0.2, 0.08]


# checking user input is correct
def chk_input(str, lst):
    chk = str
    while chk not in lst:
        chk = input("\nInvalid Input!\n Enter input:")
        print(" ")

    return chk

# TIME DELAY FUNCTIONS
# Time delay by each characters
def str_dly(str, tim_dly):

    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(tim_dly)



# Delay using a lst
def lst_dly(str_lst, tim_dly ,func = None):

    for str in str_lst:
        if func == None:
            str_dly(str, tim_dly)
        else:
            func(str)
            winsound.PlaySound("single-button-press.wav", winsound.SND_ASYNC)
            time.sleep(tim_dly)



# MAIN GAME FUNCTIONS
# Entering into GAME
def intro():
    global lst_path

    intro_lst = [ "\n","<<< EVERYTHING IS DARK >>>",
                  "You can feel around, use your hands to see.",
                  "The ground is cold, damp and covered in thick vines.",
                  "You feel a round rock that sinks into the floor when you press it.",
                  "The ground starts rumbling.", "Light begins flooding in...","\n",

                  "\n","The rock released a boulder that was blocking the cave entrance.",
                  "Three paths are revealed!","\n",

                  "Path #1: Exit forward through the caves entrance into the light.",
                  "Path #2: Explore the depths of the rear of the cave, into the darkness.",
                  "Path #3: Climb dowm the viens into a bottomless hole in the ground."

                  ]

    lst_dly(intro_lst[:8], dly[0], print)
    str_dly('"I\'m in a cave"', dly[1])
    time.sleep(dly[0])
    lst_dly(intro_lst[8:], dly[0], print)

    first_path = input("\nWhich path will you choose? (1/2/3):")
    first_path = chk_input(first_path, lst_path)

    if first_path in lst_path[:4]:
        print("\n")
        path1()
    elif first_path in lst_path[4:8]:
        print("\n")
        path2()
    elif first_path in lst_path[8:12]:
        print("\n")
        path3()

    return


def path1():

    temp_print = [ "\nYou exit forward through the cave's entrance, into the light.",
                    "It's incredibly bright but your vision adjusts as you continue.",
                    "The cave exit closes, there's no going back now.",
                    "You look out and see that you're about halfway down an incredible mountain.",
                    "A man calls out to you\n",

                    "\nThere are two paths to take to the bottom of the mountain:\n\n",
                    "Path #1: Take the set path down the mountain.","Path #2: Scale down the side of the mountain.\n\n"
                    ]

    temp_speech = [ '\n"Hello there!...\n\n',"...My name is APOLLO. I thought you were my sister, ARTEMIS...\n\n",
                    "...Ah, now I remember you! Yes, you're looking for CHRONOS...\n\n",
                     "...He's the one who trapped you in this time loop...\n\n","...Yet, I cannot bring you to him...\n\n",
                     "...Only HERMES can do that...\n\n",'...However, I have heard that CHRONOS dwells at the base of this mountain.\n\n'
                     ]

    lst_dly(temp_print[:5], dly[0], print)
    lst_dly(temp_speech, dly[1])
    lst_dly(temp_print[5:], dly[0], print)
    second_path = input("Which path will you choose? (1/2): ")
    second_path = chk_input(second_path, lst_path)

    if second_path in lst_path[:4] :
        path1_1()
    elif second_path in lst_path[4:8]:
        path1_2()

    return

def path1_1():

    temp_print = [ "\nYou begin walking down the mountain toward the bottom.",
                    "The path is long and winding but the walk is not difficult.",
                    "The sky is bright and blue and a warm breeze hits your face.\n",

                    '\n  --You think to yourself.\n',"A boy calls out to you.\n"
                    ]

    temp_speech = [ '\n"Hey! Wait up!...\n\n',"...My name is ARES. I was just coming down the mountain for some fresh air...\n\n",
                    "...Mount OLYMPUS is the highest reaching mountain on Earth and the air is specially crisp...\n\n",
                    "...Anyhow, I see you're searching for the correct path, as we all are...\n\n",
                    "...It's not my place to tell you which path is correct...\n\n", "...However, I will tell you this...\n\n",
                    '..."ONLY THROUGH DARKNESS WILL FREEDOM BE ATTAINED"\n\n'
                    ]

    lst_dly(temp_print[:3], dly[0], print)
    str_dly('  "I could get used to this..."\n\n', dly[1])
    lst_dly(temp_print[3:], dly[0], print)
    lst_dly(temp_speech, dly[1])
    print("\n\t---WRONG PATH---")
    intro()

    return

def path1_2():

    temp_print = [ "\nYou begin scaling down the side of the mountain toward the bottom.",
                    "It's a long way down but you soon grow strong enough to appreciate the view.",
                    "Although you're still about halfway up the mountain, clouds surround you and the world seems small.\n",

                    '\n  --You think to yourself',"You continue down the mountain for days until you reach the bottom.\n",

                    '\n--You yell, entering the base of Mount OLYMPUS through the largest red and black doors you\'ve ever seen\n',
                    "The darkness consumes you as you enter, unable to see a thing.","A thunderous voice calls out to you...\n"


                    ]

    temp_speech = [ "\nAh... I've been expecting you. But you're far too early..\n\n","...It appears you've taken a fairly easy route...\n\n",
                    "...You can see through the light, but not the DARKNESS...\n\n","...You've developed some STRENGTH, but not enough...\n\n",
                    "...There is more you need to grow...\n\n","...More you need to LEARN\n\n","...And learn you will\n\n","...In time...\n\n"
                    ]

    lst_dly(temp_print[:3], dly[0], print)
    str_dly('  "I don\'t believe my eyes..."\n', dly[1])
    lst_dly(temp_print[3:5], dly[0], print)
    str_dly('  "Finally! I can face you, CHRONOS!"\n', dly[1])
    lst_dly(temp_print[5:], dly[0], print)
    lst_dly(temp_speech, dly[1])
    print("\n\t---WRONG PATH---")
    intro()

    return

def path2():

    temp_print = [ "\nYou explore the depths of the rear of the cave, into the darkness.",
                    "It's incredibly dark but your vision adjusts as you continue forward.",
                    "A huge boulder slides into place behind you, blocking your path back.",
                    "You notice that the cave floor is declining to the left, like a spiral.",
                    "A woman calls out to you.\n",

                    "\nThere are two paths to continue through the cave:","Path #1: Go to the left.","Path #2: Go to the right.\n"
                    ]

    temp_speech = [ '\n"Hello there!...\n\n',"...My name is ARTEMIS... I thought you were my brother, APOLLO...\n\n",
                    "...Ah, now I remember you! Yes, you're looking for CHRONOS...\n\n","...He's the one who trapped you in this time loop...\n\n",
                    "...However, I cannot bring you to him...\n\n","...Only HERMES can do that...\n\n",
                    "...However, I have heard that CHRONOS dwells at the base of this cave...\n\n"
                    ]

    lst_dly(temp_print[:6], dly[0], print)
    lst_dly(temp_speech, dly[1])
    lst_dly(temp_print[6:], dly[0], print)

    second_path = input("Which path will you choose? (1/2):")
    second_path = chk_input(second_path, lst_path)

    if second_path in lst_path[:4] :
        path2_1()
    elif second_path in lst_path[4:8] :
        path2_2()

    return

def path2_1():

    temp_print = [  "\nYou take the fork in the cave to the left and continue walking.",
                    "The cave floor is still declining but is becoming much steeper than before.",
                    "It's so dark and the winding cave seems to go on forever.\n",

                    '\n --You think to yourself\n',
                    "Still going, fortifying your will, until finally, you reach the largest red and black door in existence.\n",

                    '\n  --You erupt as you enter the doors at the base of the cave inside Mount OLYMPUS\n',
                    "Standing now in the largest room, in front of the largest man you've ever seen.",
                    "The room is dark, but you can see the source of the thunderous voice which calls out to you...\n"
                    ]

    temp_speech = [ "\nAh... I've been expecting you. But you're still too early...\n\n","...It appears you've taken a fairly easy route...\n\n",
                    "...Your vision is keen. You see through the darkness and the light...\n\n",
                    "...However, you haven’t developed quite enough strength...\n\n","...There is more you need to grow...\n\n",
                    "...More you need to learn...\n\n","...And learn you will...\n\n","...In time.\n\n"
                    ]

    lst_dly(temp_print[:3], dly[0], print)
    str_dly("I have no choice, I must keep going...\n", dly[1])
    lst_dly(temp_print[3:5], dly[0], print)
    str_dly('  "Finally! I can face you, CHRONOS!"\n', dly[1])
    lst_dly(temp_print[5:], dly[0], print)
    lst_dly(temp_speech, dly[1])
    print("\n\t---WRONG PATH---")
    intro()

    return

def path2_2():

    temp_print = [ "\nYou take the fork in the cave to the right and continue walking.",
                    "The cave floor is now inclining and is becoming quite steep.",
                    "It's so dark but after what seems like days of walking, you see a glow in the distance.\n",

                    '\n  --You think to yourself\n',
                    "Approaching the brilliant light, you reach the end of this path and see an old book perched atop a pedestal\n",

                   ]

    temp_speech = [ '\n"If you stumble upon this tomb...\n\n',"...It may save you from your doom...\n\n",
                    "...Your vision is keen, that much is clear...\n\n","...But you have yet to face your fear...\n\n",
                    '...The truest path is one of toil..."\n\n',"...Climb down vines beneath the soil...\n\n",
                    "...Speak with MOIRAE, help her first...\n\n","...Then you will complete your search...\n\n"
                    ]

    lst_dly(temp_print[:3], dly[0], print)
    str_dly('  "What in the world can that be...?"\n', dly[1])
    lst_dly(temp_print[3:5], dly[0], print)
    str_dly('  "THE SECRETS OF TIME"\n', dly[1])
    print("\n--You read the large inscription on the cover before opening the book.\n")
    lst_dly(temp_speech, dly[1])
    print("\n\t---WRONG PATH---")
    intro()

    return


def path3():
    global lst_path

    # list for all print delay
    temp_print = [ "You climb dowm the vines into a bottomless hole in the ground.",
                   "It's dark, damp and hard to climb down the vines, but your vision and muscles eventually adjust.",
                   "A huge boulder slides into place above you, blocking your escape.",
                   "You continue climbing dowm the vines until you hear something whirring up at you.",
                   "Someone calls out your name...\n",

                   "\nHERMES will transport you anywhere on Mount OLYMPUS:\n","Path #1: Continue below to face CHRONOS.",
                   "Path #2: Read : THE SECRETS OF TIME.","Path #3: Speak with ARES.","Path #4: Speak with ARTEMIS.",
                   "Path #5: Speak with APOLLo.\n",

                   "\nYou continue down the vines until you reach the botton.",
                   "You see a small old woman next to the largest red and black iron-wrought double-doors you've ever seen.",
                   "The old woman calls out to you.\n",



                 "path #1: Forget the old woman. Enter the doors and speak with CHRONOS.",
                 "path #2: Honor the woman's request. Help MOIRAE return home safely.\n"

             ]

    # lst for speech delay
    temp_speech = [ ' "Hey, hey there!..." \n\n', "...My name is HERMES... I'll be your guide to freedom...\n\n",
                     "...Yes, I know all about you! You're looking for CHRONOS...\n\n",
                     "...He's the one who trapped you in this time loop...\n\n",
                     "...I'm on my way to deliver a message, so I can't escort you personally...\n\n",
                     "...However, I can transport you there, or  anywhere else on Mount OLYMPUS...\n\n",
                     "...CHRONOS is just below and he'll certainly TEST YOU when you meet him.\n\n",

                      '\n "Hello there!, young traveller...\n\n" \n',"...My name is MOIRAE, I'm in great need of help...\n\n",
                      "...If you enter, you may speak with him and restore your freedom...\n\n",
                      "...But before you do so, would you take me HOME?...\n\n",
                      "...I'm unable to escape this cold, dark cave on my own...","...Choice is Yours...\n\n",
                     ]

    lst_dly(temp_print[:5], dly[0], print)
    lst_dly(temp_speech[:7], dly[2])
    lst_dly(temp_print[5:11], dly[0], print)

    second_path = input("\nWhich path will you choose? (1/2/3/4/5):")
    second_path = chk_input(second_path,lst_path)

    if second_path in lst_path[4:8]:
        path2_2()
    elif second_path in lst_path[8:12]:
        path1_1()
    elif second_path in lst_path[12:16]:
        path1()
    elif second_path in lst_path[16:]:
        path2()
    else:
        lst_dly(temp_print[11:14], dly[0], print)
        lst_dly(temp_speech[7:11], dly[2])
        lst_dly(temp_print[14:], dly[0], print)
        third_path = input("Which path would you like to take? (1/2):")
        third_path = chk_input(third_path, lst_path)

        if third_path in lst_path[:4]:
            path3_1()
        elif third_path in lst_path[4:8]:
            path3_2()

    return

def path3_1():

    print("\nYou begin walking towards the doors, ignoring MOIRAE's request\n")
    time.sleep(dly[0])
    str_dly('\n"I would help you but I\'m in a bit of hurry, you understand"\n', dly[2])

    temp_print = [ "\nYou pull open the massive doors with all of your moight and enter",
                    "Standing now in the largest room, in front of the laegest man you've ever seen.",
                    "The room is dark, but you can see the source of the thunderous voice which calls out to you..."
                    ]

    temp_speech = [ "\nAh... I've been expecting you. But you're somewhat early...\n\n",
                    "...It appears you've taken a fairly hard route...\n\n",
                    "...Your vision is keen. You see through the darkness and the light...\n\n",
                    "...However, there is still just one...\n\n","...One more thing you need to learn...\n\n"
                    "...And learn you will...\n\n","...In time.\n\n"

    ]

    lst_dly(temp_print, dly[0], print)
    lst_dly(temp_speech, dly[2])
    str_dly("\n\t--- WRONG Path ---",dly[2])
    intro()

    return

def path3_2():

    print('\nYou begin walking toward MOIRAE, honoring her request\n')
    time.sleep(dly[0])

    temp_print = [ "\nYou kneel down in front of MOIRAE, allowing her to climb easily onto your back.",
                    "Standing up, you make your way back to vine wall to make your ascent.",
                    "Just as you grab the vines, the enormous red and black iron doors thrust open, slamming to a halt.",
                    "The largest man you've ever seen steps out and his thunderous voice which calls out to you...\n"

    ]

    temp_speech = [ ' \n "I understand. I know what it\'s like to miss home... That\'s why I need to get out of here..."\n\n',
                    ' "But before I walk through those doors, I promise that I\'ll get you home safely"\n\n',

                    "\nAh... I've been expecting you. And you're right on time!...\n\n",
                    "...It appears you've taken a very difficult route...\n\n",
                    "...Your vision is keen. You see through the darkness and the light...\n\n",
                    "...And your strength has grown from your travels...\n\n",
                    "...You've even put others needs before your own...\n\n",
                    "...You have learned everything I have to teach you...\n\n",
                    "...So you may finally be free...\n\n", "...It's time to return.\n"
    ]

    lst_dly(temp_speech[:2], dly[2])
    lst_dly(temp_print, dly[0], print)
    lst_dly(temp_speech[2:], dly[2])

    print("\n\t--- YOU WON ---")
    return



# printing Title Screen
print("\n")
print("     #########################")
print("     #                       #")
print("     #   Time   Unraveled    #")
print("     #                       #")
print("     #########################")
print("\n")
time.sleep(dly[0])
print("whoa.... What happened? Where am I?")
playsound("single-button-press.wav")
time.sleep(dly[0])
print("It's too dark to see anything...")
playsound("single-button-press.wav")
print("\n")

# starting the Game
start_game = input("Would you like to start the GAME?  type: yes(Y) or no(N)")
start_game = chk_input(start_game,lst_game)

if start_game in lst_game[:4] :
    intro()
elif start_game in lst_game[4:] :
    print("\n--- May be next time! ---")
    playsound("single-button-press.wav")
