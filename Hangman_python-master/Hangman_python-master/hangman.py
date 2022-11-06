# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    a = True
    b = True
    i = 0
    while a:
            if secret_word[i] in letters_guessed:
                a = True
                b = True
                i+=1
            else:
                a = False
                b = False
            if i>=len(secret_word):
                a = False
                b = True
    return b


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    l = []
    for i in range(len(secret_word)):
        l.append('_ ')

    i=0

    for s in secret_word:
        if s in letters_guessed:
            l[i]=s
        i+=1

    ans = "".join(l)
    return ans



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for e in letters_guessed:
        if e in l:
            l.remove(e)
    return "".join(l)




def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("""Welcome to Hangman!!!!!\n\nThis is an interactive game desgined by Shehraj Singh.""")
    letters_guessed = []
    g = len(secret_word)
    print('The secret word is',g,'letters long.')
    print('_ '*len(secret_word))
    while True:
        print("""Player has""",g,"""guesses remaining.\n\nThe List of letters that have not been used by player are:
        """,get_available_letters(letters_guessed))


        guess = ''

        while len(guess)!=1:
            print('Please enter a single letter')
            guess = input('Guess a letter:')

            guess = guess.lower()

            if len(guess)==1:
                letters_guessed.append(guess)

        print(get_guessed_word(secret_word,letters_guessed))


        if is_word_guessed(secret_word,letters_guessed)==True:
            print("Congrats!!!!!")
            break

        if guess in secret_word and g!=0:
            g+=1



        g-=1

        if g==0:
            print("\n\nOH! OH! .......Game is Over........")
            print('\n\nTHE CORRECT WORD WAS:',secret_word)
            break





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    l1 = my_word.split(' ')
    l2 = list(other_word)
    word = ''.join(l1)

    if len(word)!=len(other_word):
        return False

    i = 0
    for s in word :
        if s!='_' and word[i]!=l2[i]:
            return False
        i+=1
    return True


# def show_possible_matches(my_word):
#     '''
#     my_word: string with _ characters, current guess of secret word
#     returns: nothing, but should print out every word in wordlist that matches my_word
#              Keep in mind that in hangman when a letter is guessed, all the positions
#              at which that letter occurs in the secret word are revealed.
#              Therefore, the hidden letter(_ ) cannot be one of the letters in the word
#              that has already been revealed.
#
#     '''
#
#
#
#
#
#
# def hangman_with_hints(secret_word):
#     '''
#     secret_word: string, the secret word to guess.
#
#     Starts up an interactive game of Hangman.
#
#     * At the start of the game, let the user know how many
#       letters the secret_word contains and how many guesses s/he starts with.
#
#     * The user should start with 6 guesses
#
#     * Before each round, you should display to the user how many guesses
#       s/he has left and the letters that the user has not yet guessed.
#
#     * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
#
#     * The user should receive feedback immediately after each guess
#       about whether their guess appears in the computer's word.
#
#     * After each guess, you should display to the user the
#       partially guessed word so far.
#
#     * If the guess is the symbol *, print out all words in wordlist that
#       matches the current guessed word.
#
#     Follows the other limitations detailed in the problem write-up.
#     '''
#     # FILL IN YOUR CODE HERE AND DELETE "pass"
#     pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two6 lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
