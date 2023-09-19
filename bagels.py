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
    print('''Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
          
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:         That Means:
        Pico                One digit is correct but in the wrong position
        Fermi               One digit is correct and in the right position
        Bagels              No digit is correct.
        
    For Example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico'''.format(NUM_DIGITS))

    while True: #Main game loop.
        #This Stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print("You have {} guess to get it." .format(MAX_GUESSES)) #Set on the top of the code.

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            #Keep looping until they enter a valid guess.
            while len(guess) != NUM_DIGITS or not guess.isdecimal():  #len() function returns the items in a list.
                #.isdecimal returns true if all the characters are decimals(0-9)
                print('Guess #{}:'.format(numGuesses))
                guess = input('>')

            clues = getClues(guess, secretNum)
            print(clues)
            numguesses += 1

            if guess == secretNum:
                break #They're  correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses :(")
                print("The answer was {}.".format(secretNum))
                #.format() method formats the specified values and inserts thme inside the string's placeholder. Placeholder Defined By Curly Brackets : {}
            
        #Ask player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
        print("Thanks for playing !")

        def getSecretNum():
            """Returns a string made up of NUM_DIGITS unique random digits."""
            numbers = list('0123456789') # Create a list of digits 0 to 9.
            random.shuffle(numbers) #Shuffle them into random order.

            #Get the first NUM_DIGITS digits in the list for the secret number: 
            secretNum = ''
            for i in range(NUM_DIGITS):
                secretNum += str(numbers[i])
                return secretNum
            
            def getClues(guess, secretNum):
                """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
                if guess == secretNum:
                    return ' You Got it !'
                
                clues = []
                
                for i in range(len(guess)):
                    if guess[i] == secretNum[i]:
                        #A Correct digit is in the correct placre.
                        clues.append('Fermi')
                    elif guess[i] in secretNum:
                        #A Correct digit is in the incorrect place.
                        clues.append('Pico')
                        if len(clues) == 0:
                            return 'Bagels' #There are no correct digits at all 
                        else:
                            #Sort the clues into alphabetical order so their original order doesn't give any information.
                            clues.sort()
                            #Make a Single string from the list of string clues.
                            return ' '.join(clues)
                        
                        #if the program is run (instead of imported), run the game:
            if __name__ == '__main__':
                main()