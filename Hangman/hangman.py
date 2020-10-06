import pygame
import math

# Initializing the game
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tinku's Hangman")

# Load images
images = []
for i in range(6):
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
LETTER_FONT = pygame.font.SysFont("helvitica", 40)
WORD_FONT = pygame.font.SysFont("helvitica", 60)
TITLE_FONT = pygame.font.SysFont("helvitica", 70)

# game variables
hangman_status = 0
word = "DEFAULT"
words = ["ABRACADABRA", "SIDUSH", "GENIE"]
guessed = []

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


""" MAIN PROGRAM """
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    # draw TITLE_FONT
    text = TITLE_FONT.render("Tinku's Hangman", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_wrd = ""
    for letter in word:
        if letter in guessed:
            display_wrd += letter + " "
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


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("--- YOU WIN ---")
        break

    if hangman_status == 6:
        display_message("--- YOU LOSE ---")
        break


pygame.quit()
