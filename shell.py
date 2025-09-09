import os

letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 
            'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}


def word_empty(word):
    return len(word) == 0


def insert_word():
    print("Welcome to the hangman game! Hope you enjoy it!")

    continue_loop = True
    word = None
    while(continue_loop):
        word = input("Insert the word please: ").lower()
        if word_empty(word):
            print("The word can't be empty.")

        letters_word = set(word)
        has_invalid = False
        for letter in letters_word:
            if letter not in letters.keys():
                print(f"Sorry but the character {letter} is not valid.")
                has_invalid = True

        if has_invalid == False:
            confirmation = input(f"\nThe word selected is \"{word}\". Is correct? (Y/N): ").upper()

            if confirmation == "Y": 
                continue_loop = False

    os.system("clear")
    print("The word has been choosen. Good luck!")
    
    return list(word)


def submit_letter():
    continue_loop = True
    char = None
    while(continue_loop):
        char = input("\n\nInsert the letter please: ").lower()

        if word_empty(char):
            print("The letter can't be empty.")
        
        elif char not in letters.keys():
            print("Select a valid letter please.")

        elif letters[char] == 1:
            print("The letter was already selected before.")

        else:
            confirmation = input(f"\nThe letter selected is \"{char}\". Is correct? (Y/N): ").upper()

            if confirmation == "Y": 
                letters[char] = 1
                continue_loop = False

    return char

def print_word(word):
    for char in word:
        print(f"{char} ", end="")
    
    print()