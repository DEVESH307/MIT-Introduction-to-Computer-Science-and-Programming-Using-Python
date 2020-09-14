# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random,string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    my_String = ''
    for x in secretWord:
        if x in lettersGuessed:
            my_String += x
        else:
            my_String += '_'
    return my_String



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    notGuessed = ''
    for x in 'abcdefghijklmnopqrstuvwxyz':
        if x not in lettersGuessed:
            notGuessed += x
    return notGuessed


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = [] 
    mistakeMade = 0 
    availableLetters = string.ascii_lowercase   
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %s letters long." % (len(secretWord))

    while mistakeMade <9:
        print '-------------'
        if isWordGuessed(secretWord, lettersGuessed):
            print "congratulations, you won!"
            break
        if mistakeMade == 8:
            print "Sorry, you ran out of guesses. The word was %s" % (secretWord)
            break

        print "You have %s guesses left." % (8-mistakeMade)
        print "Available letters: " + availableLetters

        tmp = raw_input("Please guess a letter: ").lower()

        if tmp in lettersGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(tmp)
            availableLetters = getAvailableLetters(lettersGuessed)


            if tmp in secretWord:
                print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)

            else:
                print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
                mistakeMade +=1


hangman('cheetah')
hangman('test')

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# harder input cases.
# 1. Testing if we can correctly fill in repeat letters and handle capitalized input ...
# 2. Testing if we handle repeat incorrect guesses...
# 3. Testing if we can correctly guess a word...
# 4. Testing if we run out of guesses...
# 5. Testing if we can correctly fill in multiple letters...
# 6. Testing if we correctly handle repeat guesses...
