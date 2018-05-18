import random
import string
import os
import sys
from classes.word import Word


def reloadIfGreater(guesses, diff):
    while(guesses < diff):
        new_inFile = open(WORDLIST_FILENAME, 'r')
        new_line = new_inFile.readline()
        new_wordlist = str.split(new_line)
        hangman(random.choice(new_wordlist))

def initialPresentation(secretWord):
    response = ''
    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')

    try:
        response = input('Would you like to know how many different letters the word has? (y/n) ')

    except KeyboardInterrupt:
        print('\nYou cancelled the operation.')
        sys.exit()

    while (response != 'y') and (response != 'n'):
        response = input('Would you like to know how many different letters the word has? (y/n) ')
    if(response == 'y'):
        print('The word has', differentLetters(secretWord), 'different letters')
    else:
        pass

    print('-------------')


def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True


def getAvailableLetters():
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    return available


def letterInWord(secretWord, lettersGuessed):
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '

    return guessed


def differentLetters(secretWord):
    diffnumber = 0
    for letter in getAvailableLetters():
        if letter in secretWord:
            diffnumber += 1

    return diffnumber


def hangman(secretWord):

    try:
        guesses = 8
    except NameError:
        print('\nVariable guesses must be a number')
        sys.exit()

    reloadIfGreater(guesses, differentLetters(secretWord))
    lettersGuessed = []
    initialPresentation(secretWord)

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print('You have ', guesses, 'guesses left.')

        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print('Available letters', available)

        try:
            letter = input('Please guess a letter: ')

        except KeyboardInterrupt:
            print('\nYou cancelled the operation.')
            sys.exit()

        while letter.isalpha() == False:
            letter = input('You can only type letters: ')

        if letter in lettersGuessed:

            guessed = letterInWord(secretWord, lettersGuessed)

            print('Oops! You have already guessed that letter: ', guessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = letterInWord(secretWord, lettersGuessed)

            print('Good Guess: ', guessed)
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = letterInWord(secretWord, lettersGuessed)

            print('Oops! That letter is not in my word: ',  guessed)

        print('------------')

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. The word was ', secretWord, '.')
    quit()

start_word = Word()
start_word.iftxtFile()
hangman(start_word.loadWords().lower())
