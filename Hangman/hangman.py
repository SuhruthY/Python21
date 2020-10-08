import pygame
import math
import random

# Initializing the game
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tinku's Hangman")
ICON = pygame.image.load("hangman.png")
pygame.display.set_icon(ICON)


## Global Variables
# Load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) +".png")
    images.append(image)

# button variables
RADIUS = 20
GAP = 15
letters = []
start_x = round((WIDTH - (GAP + RADIUS * 2) *13) / 2)
start_y = 400
A = 65
for i in range(26):
    x = start_x + GAP * 2 + ((GAP + RADIUS * 2) * (i % 13))
    y = start_y + (i // 13) * ((GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
BUTTON_FONT = pygame.font.SysFont("helvitica", 30)
LETTER_FONT = pygame.font.SysFont("helvitica", 40)
WORD_FONT = pygame.font.SysFont("helvitica", 50)
TITLE_FONT = pygame.font.SysFont("helvitica", 70)
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)

# game variables
hangman_status = 0
#word = "DEFAULT"
guessed = []
winning_count = 0
no_of_times = 0
pause = False


# Picking a Random word
words = []
f_lst = ["words", "words2", "words3"]
f_name = random.choice(f_lst)
with open(f_name + ".txt", "r") as fh:
    lines = fh.readlines()
    for line in lines:
        wrds = line.split()
        for wrd in wrds:
            wrd = wrd.upper()
            words.append(wrd)
words = list(set(words))
#print(words)


# Functions
# Refresh Necessary Variables
def refresh():
    global hangman_status
    global guessed
    global letters
    global word

    hangman_status = 0
    word = random.choice(words)
    guessed = []

    letters = []
    start_x = round((WIDTH - (GAP + RADIUS * 2) *13) / 2)
    start_y = 400
    A = 65
    for i in range(26):
        x = start_x + GAP * 2 + ((GAP + RADIUS * 2) * (i % 13))
        y = start_y + (i // 13) * ((GAP + RADIUS * 2))
        letters.append([x, y, chr(A + i), True])

# draw on window
def draw():
    global hangman_status
    global guessed
    global letters

    win.fill(WHITE)
    text = TITLE_FONT.render("Tinku's Hangman", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_wrd = ""
    for letter in word:
        if letter in guessed :
            display_wrd += letter + " "
        elif letter == "-":
            display_wrd += "  "
        else:
            display_wrd += "_ "
    text = WORD_FONT.render(display_wrd, 1, BLACK)
    win.blit(text, (400, 200))

    # draw letters
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_width() / 2))

    win.blit(images[hangman_status],(150,100))
    pygame.display.update()

# display given messsage
def display_message(msg):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(msg, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

# Create a button
def button(msg, rect_par, def_col, color, action = None):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x_pos, y_pos, width, height = rect_par

    if x_pos < mouse_pos[0] < x_pos + width and y_pos < mouse_pos[1] < y_pos + height :
        pygame.draw.rect(win, def_col, (x_pos, y_pos, width, height))
        if click[0] == 1 and action != None:
            action()
    else :
        pygame.draw.rect(win, color, (x_pos, y_pos, width, height))

    text = BUTTON_FONT.render(msg, True, BLACK)
    boundary = text.get_rect()
    boundary.center = ( (x_pos + (width /2)), (y_pos +(height/2)) )
    win.blit(text, boundary)

# quit Function
def game_quit():
    pygame.quit()
    quit()

# unpause function
def unpause():
    global pause
    pause = False

# Pause Function
def game_pause():
    win.fill(WHITE)
    text = TITLE_FONT.render("Game Paused", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/4))

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        button("Continue", (250,200,100,50), BRIGHT_GREEN, GREEN, unpause)
        button("Quit", (450,200,100,50), BRIGHT_RED, RED, game_quit)

        pygame.display.update()

def game_over():
    win.fill(WHITE)
    text = TITLE_FONT.render("Game Over", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/4))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Restart", (250,200,100,50), BRIGHT_GREEN, GREEN, main)
        button("Quit", (450,200,100,50), BRIGHT_RED, RED, game_quit)

        pygame.display.update()
        refresh()


# Intro function
def game_intro():
    INTRO = True

    while INTRO:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill(WHITE)
        text = TITLE_FONT.render("Tinku's Hangman", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/4))

        button("Start", (250,200,100,50), BRIGHT_GREEN, GREEN, main)
        button("Quit", (450,200,100,50), BRIGHT_RED, RED, game_quit)

        pygame.display.update()
        refresh()

# GAME LOOP
def main():
    global pause
    global hangman_status
    global guessed
    global letters
    global word

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game_quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    game_pause()

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status +=1

        draw()

        # checking your won
        won = True
        for letter in word:
            if letter != "-":
                if letter not in guessed:
                    won = False
                    break

        if won:
            display_message("--- YOU WIN ---")
            break

        if hangman_status == 6:
            display_message("The word is " + word)
            hangman_status = 0
            display_message("--- YOU LOSE ---")
            game_over()
            break

## --- MAIN PROGRAM ---

game_intro()

pygame.quit()
quit()
