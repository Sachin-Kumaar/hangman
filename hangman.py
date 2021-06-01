import random
import os
import sys
os.system("cls")


WORDLIST_FILENAME = "words.txt"
with open(WORDLIST_FILENAME) as w:
    word_bank = w.read().split()
    print("Loading word list from file...")
    print(len(word_bank), " words loaded.")
    print("Welcome to Hangman Ultimate Edition")

def choose_random_word(all_words):
    return random.choice(all_words)
    pass

def load_words():
    pass

alp=""
for idx in range(97, 97 + 26): 
    alp = alp + chr(idx)


def first(bad_guesses, good_guesses, secret_word, strikes, alp):
    """The basic view given to the user whilst playing"""
    print("I am thinking of a word that is {} letters long".format(len(secret_word)))
    print("-------------")
    print("you have {} guess left".format(strikes-len(bad_guesses)))
    print("Available letters: {}".format(alp))
def daw(bad_guesses, good_guesses, secret_word):
    
    print("".join([char if char in good_guesses else '_ ' for char in secret_word]))


def draw(bad_guesses, good_guesses, secret_word, strikes, guess, alp):
    """The basic view given to the user whilst playing"""
    print("-------------")
    print("you have {} guess left".format(strikes-len(bad_guesses)))
    #" ".join([char for char in bad_guesses]), end="\n\n\n"
    bad_guesses=set(bad_guesses)
    good_guesses=set(good_guesses)
    print("Available letters: ",end='')
    alp=set(alp)
    alp=alp-bad_guesses
    alp=alp-good_guesses
    alp=sorted(alp)
    print("".join(alp))
    

    


def get_guess(bad_guesses, good_guesses, secret_word, strikes):
    """Requests and validates input from user"""
    while True:
        guess = input("Please guess a letter: \u001b[31m").lower().strip()
        print("\u001b[37m",end="")
        if len(guess) != 1:
            print("You must only guess a single letter!",end='')
            daw(bad_guesses, good_guesses, secret_word)
            draw(bad_guesses, good_guesses, secret_word, strikes, guess, alp)
        elif guess in bad_guesses or guess in good_guesses:
            print("Oops! You've already guessed that letter: ",end='')
            daw(bad_guesses, good_guesses, secret_word)
            draw(bad_guesses, good_guesses, secret_word, strikes, guess, alp)
        elif not guess.isalpha():
            print("You can only guess letters!",end='')
            daw(bad_guesses, good_guesses, secret_word)
            draw(bad_guesses, good_guesses, secret_word, strikes, guess, alp)
        else:
            return guess
  
    


def hangman():
    """Main loop that calls all other functions"""
    
    secret_word = random.choice(word_bank)
    
    good_guesses = []
    bad_guesses = []
    strikes = 6
    first(bad_guesses, good_guesses, secret_word, strikes, alp)
    while True:
        
        
        guess = get_guess(bad_guesses, good_guesses, secret_word, strikes)
        
        # Add letter to good guesses and check if player wins
        if guess in secret_word:
            good_guesses.append(guess)
            
            print("Good guess: ",end='')
            daw(bad_guesses, good_guesses, secret_word)
            #print("------------")
            if len(good_guesses) == len(set(secret_word)):
                draw(bad_guesses, good_guesses, secret_word, strikes, guess, alp)
                print("Congratulations, you won!")
                print("Your total score for this game is: {}".format(strikes))
                break

        # Add letter to bad guesses and check if player loses
        else:
            bad_guesses.append(guess)
            print("Oops! That letter is not in my word: ",end='')
            daw(bad_guesses, good_guesses, secret_word)
            print(end='')
            #print("------------")
            if len(bad_guesses) == strikes:
                print("-------------------")
                print("Sorry, you ran out of guesses. The word was: {}".format(secret_word))
                break
        draw(bad_guesses, good_guesses, secret_word, strikes, guess, alp)
def main():
    hangman()


if __name__ == "__main__":
    main()