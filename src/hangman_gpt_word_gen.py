import sys
from os.path import abspath, dirname

# Add the parent directory of the current file to sys.path
sys.path.append(abspath(dirname(dirname(__file__))))

from include import gpt

def gen_word(language):
    prompt = f"""I'm going to play a game of hangman.
Your task is to give me a random word that is not too difficult for me to guess.
Your answer should be only the word and nothing else.
Furthermore, choose a word in {language}.
Avoid using words with accent if that is commo in the given language."""

    gened_word =  gpt.get_completion(prompt)
    return gened_word.strip().replace('\n', '').replace('.', '').lower()