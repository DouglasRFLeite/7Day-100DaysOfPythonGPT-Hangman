# 7Day-100DaysOfPythonGPT-Hangman
Day 7 of the [100 Days of Code with Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) from Udemy.

## What is 100DaysOfPythonGPT?

100 Days of Python is a Python Bootcamp from Udemy that provides 100 days of Python pratical content with lessons and projects. The GPT part is something I'm adding to the course and infers that I shall use ChatGPT's engine and/or API in some way on each and every one of those 100 projects. Furthermore, I shall also practice using PyTest to test these projects and applications at least in some level.

## Hangman

Hangman is the fifth project of the fifth day of the bootcamp. Its original purpose is to use remember everything that has been done.

As the name says, it is a game of Hangman, where the game selects a random word and the user/player tries to guess it letter by letter while a man in beeing drawed hanging.

ChatGPT's API was used to substitute generate the random word. Originally there was a list of word provided in the bootcamp, but GPT has more creativity. Besides, I also used it to add the possibility to use words from any language. In the end I noticed the API was returning the word with a lot of spaces and even ponctuation, so I had to remove it and it worked. 

## Project Structure

 - [src/](src/) - The `hangman.py` file holds the game functionality, `hangman_art.py` has the ASCII art used in the game for the logo and the hang and the function that prints it, `hangman_wordlist.py` has the list of words and the name generation function that chooses from it, whilst `hangman_gpt_word_gen.py` has a function with the same name that recieves a language and generates a word in that language;
 - [include/](include/) - The `gpt.py` file holds the `get_completion` function that accesses the ChatGPT API. 
