#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program creates a number guessing game

import constants


def main():
    # this function creates the game

    # input
    number_guessed = int(input("Enter the number between 0 - 9: "))

    # process
    if number_guessed == constants.CORRECT_NUMBER:
        print("You guessed correct!")
    else:
        print("You guessed wrong!")

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
