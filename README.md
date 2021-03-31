# First Fifty
&nbsp;&nbsp;&nbsp;&nbsp;*First Fifty* is a collection of python projects ranging all levels of experience in python.
We will be working with search algorithms, simulations, text searching and parsing, mini-games, full length games, frameworks, etc in this set of projects.
I fell as a beginner project-based learning provided you with much more knowledge about real-world environment. You will have a greater scope to experiment 
with the techniques and come up with new ideas.   

&nbsp;&nbsp;&nbsp;&nbsp;Here in this page I'm going to explain about what each and every project is about, it's boundaries, scopes and how can you change it,
and provide some references for further study.

## Easy Bundle
&nbsp;&nbsp;&nbsp;&nbsp;The *Easy Bundle* is a set of simple python mini-projects which uses basic python fundamentals. It comprises of projects like  

### [Binary Search][1]:   
<img align="left" width="200" height="200" src="https://cdn.techterms.com/img/lg/binary_14.jpg">  
Binary search looks for a particular item by comparing the middle most item of the collection. If a match occurs, then the index of item is returned. If the middle item is greater than the item, then the item is searched in the sub-array to the left of the middle item. Otherwise, the item is searched for in the sub-array to the right of the middle item. This process continues on the sub-array as well until the size of the subarray reduces to zero.  

&nbsp;    
For this algorithm to work properly, the data collection should be in the sorted form.    

<br><br>

####  [Dice Simulator][2]:  
<img align="right" width="300" height="200" src="https://images.pexels.com/photos/4052295/pexels-photo-4052295.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"> 
As the name suggests, we will be simulating a rolling dice. This is one of the interesting python projects and will generate a random number each dice the program runs, and the users can use the dice repeatedly for as long as he wants. When the user rolls the dice, the program will generate a random number between 1 and 6 (as on a standard dice).  

&nbsp;  
I used the command line to simulate the dice but you can go a step further creating a simple GUI.

<br><br>

### [Leap it!][4]:  
&nbsp;&nbsp;&nbsp;&nbsp;For a given input a year you neeed to check whether it is a leap year or not. For this, you’ll have to create a function that recognizes the pattern of leap years and can try fitting the inputted year into the pattern. In the end, you can print the result using a boolean expression.   
&nbsp;  
The thing that is challengng here is to making sure the user enters only years(4-digit integer)  

### [Find out, Fibonacci!][3]:  
&nbsp;&nbsp;&nbsp;&nbsp;For a given input a number and the function created checks whether the number belongs to the Fibonacci sequence or not. The underlying program works are similar to the above ‘Leap it!’ program.  

### [Number Guessing][5]:
&nbsp;&nbsp;&nbsp;&nbsp;The computer will generate a random number between 1 and 100 and the user needs to guess it. If the guess is wrong then you will be provided with a clue saying the number you guessed is greater or lesser than the original number. You can use the random module in python to complete this project.  

### [Desktop Notifier][6]:  
&nbsp;&nbsp;&nbsp;&nbsp;The desktop notifier apps run on your system and send you a piece of information after a fixed interval of time. I suggest you to use libraries such as notify2, requests, etc. to build such a program. 

&nbsp;  
I personally used the *ToastNotifier* class from the python [win10toast][21] library to finish this project.    

### [Rock, Paper and Scissors][7]:  
<img align="left" width="200" height="200" src="https://miro.medium.com/max/612/1*G9UfaUBS_VqtFILMe37fZw.jpeg"> 
The a 5-minute stint of rock, paper, scissors with the computer and designed by you, yourself will improve your mood. 

&nbsp;  
We again use the random function here. You make a move first and then the program makes one. To indicate the move, you can either use a single alphabet or input an entire string. A function will have to be set up to check the validity of the move.  

&nbsp;   
Using another function, the winner of that round is decided. You can then either give an option of playing again or decide a pre-determined number of moves in advance. A scorekeeping function will also have to be created which will return the winner at the end.  

<br><br> 

### [Tic Tac Toe][8]:  
<img align="right" width="200" height="200" src="https://miro.medium.com/max/612/1*G9UfaUBS_VqtFILMe37fZw.jpeg"> 
The players create a 3×3 square grid.While the first player puts “X” in any one of the squares, and the second player will put an “O” in any square. 
This process will continue until all the squares are filled with each player putting X and O alternatively. The player who succeeds in creating a horizontal, vertical, or diagonal with three consecutive X or O on the grid wins.  

&nbsp;  
I refer the [TicTacToe][22] by clever programmer to create the complete project. All it require is to build various python functions and hence it used the terminal to run the game.  

&nbsp;   
You can go further one step and make a simple GUI using the Tkinter library.  

## Madlibs  
&nbsp;&nbsp;&nbsp;&nbsp;Madlibs is a phrasal template word game which consists of one player prompting others for a list of words to substitute for blanks in a story before reading aloud. 
- This was my first project after watching some beginner python videos. Hence I didn't got that deep into it.
- I just created a simple madlib which will generate a sentence using the input words.

## EmailSlicer   
&nbsp;&nbsp;&nbsp;&nbsp;Email Slicer is nothing but just a tool which will take an email id as an input and will perform slicing operations on it to return the username and the domain of the email id.  
- I build this project based on the [*the Guardian Pattern*][23] lecture that I watched in the PY4E course.  

## Text-Based Adventure Game  
&nbsp;&nbsp;&nbsp;&nbsp;This is a basic version of the Adventure game. It is completely text-based.  

### My Game Theme: [Time-Unraveled][10] 
&nbsp;&nbsp;&nbsp;&nbsp; In this game the main character has to find out his way out of the dark cave into the green land using the clues provied in the text. 
On his way he will meet many people who will help or obstruct him to reach his final destination. All he needs is to pick up the right choice.

- You can go with any story that you like but make sure to make this game on command line so it will have that old-school look.  
- Some other stories ans themes can be found here: [10 modern text-based adventures][24]  


## Story Generator
&nbsp;&nbsp;&nbsp;&nbsp;The program will ask users for inputs such as the name of a place, action, etc. and then build a story around the data. The story will be the same always but with little variation with the input.
- I personally used the *Stanford-NER tagger* and *Stanford-POS tagger* inorder to attach correct parts of speech in the story I generate.
- Firstly, you need to download [model jars for NER][25] and [model jars for POS][26] to integrate this with python, using install java.
- Secondly I used the `BeautifulSoup library` from python and `Pandas` to collect some movie data. 
- Then I used the python module [`nltk`][27] to tokenize the plot of each movie and collected some words with thier parts of speech.
- Finally I used some functions to replace the plots with some new words and create a new story.
 




[1]: https://github.com/SuhruthY/FirstFifty/blob/master/EasyBundle/BinarySearch.py
[2]: https://github.com/SuhruthY/FirstFifty/blob/master/EasyBundle/DiceSim.py
[3]: https://github.com/SuhruthY/FirstFifty/blob/master/EasyBundle/Fibonacci.py
[4]: https://github.com/SuhruthY/FirstFifty/blob/master/EasyBundle/LeapIt.py
[5]: https://github.com/SuhruthY/FirstFifty/blob/master/EasyBundle/GuessNum.py
[6]: https://github.com/SuhruthY/FirstFifty/blob/master/EasyBundle/DesktopNotifier.ipynb
[7]: https://github.com/SuhruthY/FirstFifty/blob/master/EasyBundle/RckPapSics.py
[8]: https://github.com/SuhruthY/FirstFifty/blob/master/EasyBundle/TicTacToe.py
[9]: https://github.com/SuhruthY/FirstFifty/blob/master/StoryGenerator/StoryGenerator.ipynb
[10]: https://github.com/SuhruthY/FirstFifty/blob/master/TextAdv/TimeUnraveled.py
[20]: https://www.calculator.net/dice-roller.html
[21]: https://pypi.org/project/wintoast/
[22]: https://www.youtube.com/watch?v=BHh654_7Cmw 
[23]: https://www.youtube.com/watch?v=WU6_0A9zYRA
[24]: https://www.gameinformer.com/b/features/archive/2017/02/12/10-modern-text-adventures-you-should-check-out.aspx
[25]: https://nlp.stanford.edu/software/stanford-corenlp-latest.zip
[26]: https://nlp.stanford.edu/software/stanford-tagger-4.2.0.zip
[27]: https://www.nltk.org/
