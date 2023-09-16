#Project 1: Deductive logic game -- 
#You must guess a secret three-digit number based on clues ! 
# "Pico" -- Your guess has a correct digit in the wrong place
# "Fermi" -- Your guess has a correct digit in the correct place
# "Bagels" -- No correct digits

"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https:nostarch.com/big-book-small-python-projects
A aversion of this game is featured in the book "Invent Your own computer games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle """

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    