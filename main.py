import os
from knower import Knower
from guesser import Guesser
from shell import insert_word, print_word, submit_letter

def main():
    player1 = Knower()
    player1.word = insert_word()

    player2 = Guesser(len(player1.word))

    while(player2.lives != 0 and player1.word != player2.word):
        print_word(player2.word)
        char = submit_letter()

        hit = False
        for i in range(len(player1.word)):
            if(player1.word[i] == char):
                player2.word[i] = char
                hit = True

        if hit == False:
            player2.lives -= 1
            print(f"You have {player2.lives} lives left.\n")

    if (player2.lives == 0):
        print(f"Sorry you have lost the game. The word choosen was \"", end="")

        for char in player1.word:
            print(f"{char}", end="")

        print("\".\n")
    
    else:
        print("Congratulations, you have won!")


if __name__ == "__main__":
    main()