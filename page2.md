## Text-Based Adventure Game  
&nbsp;&nbsp;&nbsp;&nbsp;This is a basic version of the Adventure game. It is completely text-based.  

### My Game Theme: [Time-Unraveled][0] 
&nbsp;&nbsp;&nbsp;&nbsp; In this game the main character has to find out his way out of the dark cave into the green land using the clues provied in the text. 
On his way he will meet many people who will help or obstruct him to reach his final destination. All he needs is to pick up the right choice.

- You can go with any story that you like but make sure to make this game on command line so it will have that old-school look.  
- Some other stories ans themes can be found here: [10 modern text-based adventures][24]  

## [Story Generator][1]
&nbsp;&nbsp;&nbsp;&nbsp;The program will ask users for inputs such as the name of a place, action, etc. and then build a story around the data. The story will be the same always but with little variation with the input.
- I personally used the *Stanford-NER tagger* and *Stanford-POS tagger* inorder to attach correct parts of speech in the story I generate.
- Firstly, you need to download [model jars for NER][25] and [model jars for POS][26] to integrate this with python, using install java.
- Secondly I used the `BeautifulSoup library` from python and `Pandas` to collect some movie data. 
- Then I used the python module [`nltk`][27] to tokenize the plot of each movie and collected some words with thier parts of speech.
- Finally I used some functions to replace the plots with some new words and create a new story.  

## [Video Downloader][2]  
&nbsp;&nbsp;&nbsp;&nbsp;




&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[**`previous page`**][24] 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[**`next page`**][25]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                     


[0]: https://github.com/SuhruthY/FirstFifty/blob/master/TextAdv/TimeUnraveled.py
[1]: https://github.com/SuhruthY/FirstFifty/blob/master/StoryGenerator/StoryGenerator.ipynb
[2]: https://github.com/SuhruthY/FirstFifty/blob/master/VideoDownloader/VideoDownloader.ipynb
[3]:


[24]: https://www.gameinformer.com/b/features/archive/2017/02/12/10-modern-text-adventures-you-should-check-out.aspx
[25]: https://nlp.stanford.edu/software/stanford-corenlp-latest.zip
[26]: https://nlp.stanford.edu/software/stanford-tagger-4.2.0.zip
[27]: https://www.nltk.org/
[24]: https://suhruthy.github.io/FirstFifty/
[25]: https://suhruthy.github.io/FirstFifty/page2