# How I created a Hangaman game using pygame?
Hi, welcome to *Code walk-thorugh* by SuhruthY.

This is completely a code walkthrough of my *Hangman project* you can find detailed explanation of games rules, resources, code files, etc on [readme page](https://suhruthy.github.io/FirstFifty/) or [code sample](https://github.com/SuhruthY/FirstFifty/blob/master/Hangman/hangman.py).
&nbsp;
### Installing  and Intializing pygame:
- Type this command on your terminal.
```python
pip install pygame
```
---
```
Collecting pygame
  Downloading https://files.pythonhosted.org/packages/01/da/4ff439558641a26dd29b04c25947e6c0ace041f56b2aa2ef1134edab06b8/pygame-2.0.1-cp36-cp36m-manylinux1_x86_64.whl (11.8MB)
     |████████████████████████████████| 11.8MB 4.5MB/s 
Installing collected packages: pygame
Successfully installed pygame-2.0.1
```
- First import the module pygame.
- Start with the code as shown below and don't forget to quit pygame.
```python
import pygame
pygame.init()
...
...
pygame.quit()
quit()
```
&nbsp;
## Intializing Hangman:
- While  initializing the game make sure you choose proper width and heights (in this case I choose a width of 800 and a height of 500).
- You can also add capitons and icons at this stage. 
```python 
# Initializing the game
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tinku's Hangman")
ICON = pygame.image.load("hangman.png")
pygame.display.set_icon(ICON)
```
note: you can download free icons from [flat-icon](https://www.flaticon.com/) but make sure you download the license or attribute them.
&nbsp;
## GLobal variables
### loading words list and images
- Here I'm choosing a random file and loading all of the words into words list.
```python
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
``` 
- Here I'm loading all of the neccessary images for the game.
```python 
# Load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) +".png")
    images.append(image)
```
### Buttons:
- You can choose any shape to your buttons. Here we are making round ones.
- We are choosing the radius and gap between each to be 20(px) and 15(px) respectively
- The other calculations should be adjusted according to the Width and height to defined above.
``` python
import math
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
```
note: If you are using your own shape , then make are adding all of the alphabets and fit them to your screen.
### Game variables
- These variables will be changed during the game play.
```python
# game variables
hangman_status = 0
guessed = []
winning_count = 0
no_of_times = 0
pause = False
```
### Others
- There are other variables like fonts and colors which I'm leaving to you to choose.
- But check the syntax below to creating a font or color. \
```markdown
## fonts
 pygame.font.SysFont("font_name", 30)
 eg: BUTTON_FONT = pygame.font.SysFont("helvitica", 30)

## colors
NAME = (R, G. B)
eg: 
1. WHITE = (255, 255, 255)
2. BLACK = (0, 0, 0)
```

