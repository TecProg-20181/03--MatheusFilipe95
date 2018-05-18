import random
import string

class Word:

    def __init__(self):
        self.inFile = ''
        self.line = ''
        self.wordlist = ''
        self.WORDLIST_FILENAME = "palavras.txt"

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print("Loading word list from file...")
        # inFile: file
        inFile = open(self.WORDLIST_FILENAME, 'r')
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = str.split(line)
        print("  ", len(wordlist), "words loaded.")
        return random.choice(wordlist)

    def iftxtFile(self):
        if self.WORDLIST_FILENAME.endswith('.txt'):
            return True
        else:
            exit()
