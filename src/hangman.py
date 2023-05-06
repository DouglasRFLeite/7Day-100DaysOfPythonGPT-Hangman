from hangman_art import print_logo, print_stage
#from hangman_wordlist import gen_word
from hangman_gpt_word_gen import gen_word

def update_hidden_word(word, hidden_word, letter):
    was_right = False
    for i, let in enumerate(word):
        if letter == let:
            hidden_word = hidden_word[:i] + letter + hidden_word[i+1:]
            was_right = True
    return hidden_word, was_right

def hangman():
    print_logo()
    language = input("What language do you want the word to be in:  ")
    word = gen_word(language)
    hidden_word = ("-"*len(word))
    lives = 6
    while (word != hidden_word) and (lives > 0):
        print_stage(lives=lives)
        print(hidden_word)
        letter = input("Try one letter: ").lower()
        hidden_word, was_right = update_hidden_word(word, hidden_word, letter)
        if not was_right:
            lives -= 1
        print()
    
    if lives > 0:
        print(hidden_word)
        print(f"Congratulations! You got '{word}' right!")
    else:
        print_stage(lives)
        print(f"You lose! I'm sorry, the word was '{word}'...")



if __name__ == "__main__":
    hangman()