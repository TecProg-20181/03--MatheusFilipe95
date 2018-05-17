import random
import string

WORDLIST_FILENAME = "palavras.txt"

class Word:

    def __init__(self):
        self.inFile = ''
        self.line = ''
        self.wordlist = ''

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print("Loading word list from file...")
        # inFile: file
        inFile = open(WORDLIST_FILENAME, 'r')
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = str.split(line)
        print("  ", len(wordlist), "words loaded.")
        return random.choice(wordlist)
