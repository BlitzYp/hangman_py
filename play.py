import pyfiglet
import random
from lib import stages, word_list
from time import sleep
from termcolor import colored

if __name__ == "__main__":
    try:
        word_chosen = random.choice(word_list)
        lives = len(stages) - 1
        print(pyfiglet.figlet_format("Hangman"))
        display_word = ['_' for _ in range(len(word_chosen))]
        guessed = {}
        while True:
            print(stages[lives])
            printed = " ".join(display_word)
            print(f"Lives {lives}\nword: {printed}")
            guess = input("Your guess?: ")
            if guessed.get(guess): 
                print(colored("Already guessed...", color="red"))
                continue
            guessed[guess] = True
            if guess not in word_chosen:
                lives -= 1
                print(f"Uh oh, the letter {guess} was incorrect!")
                if lives == 0:
                    print(colored(stages[lives], color="red"))
                    won = False
                    break 
            else:
                for i in range(len(word_chosen)):
                    if guess == word_chosen[i]:
                        display_word[i] = guess
                if '_' not in display_word:
                    won = True
                    break
        if won: print(pyfiglet.figlet_format(f"You won! : The word was {word_chosen}"))
        else: print(pyfiglet.figlet_format(f"You lost!: The word was {word_chosen}"))
    except ValueError:
        print("incorrect value!")
        
