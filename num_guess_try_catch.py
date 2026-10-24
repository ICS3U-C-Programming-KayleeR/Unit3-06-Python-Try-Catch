#!/usr/bin/env python3
# Created By: Kaylee Ralejoe
# Date: 17,10,2026
# The program generates a random
# number from a range of numbers and creates
# a guessing game for the user to
# guess what the number may be.
# The program has error handling in case the
# user inputs an invalid character.


import random


def main():
    # Generate random number
    randomNum = random.randint(1, 10)

    # Get user guess
    guessed_number_string = input("Guess a number from (1-10): ")

    # Try and compare user guess to randomly generated number
    try:
        guessed_number_as_int = int(guessed_number_string)
    except:
        print("{} is not a valid integer".format(guessed_number_string))
    else:
        if guessed_number_as_int == randomNum:
            print("You guessed correctly!")
        else:
            print("You guessed wrong, the correct answer is {}".format(randomNum))


if __name__ == "__main__":
    main()
