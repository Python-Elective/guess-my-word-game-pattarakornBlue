
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    '''
    for every letter that is guessed
     if all letter is not part of secret word
      return False
    otherwise return true
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
          return False
    return True
        


### Testcases
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    '''
    for every letter in secret word
      if letter is in guess letter
        print the letter
      if not
        print _
    '''
    word = ""
    for letter in secret_word:
      if letter in letters_guessed:
        word += letter
      else:
        word += ' _ '
    return word
    
    
    
    
      
#Testcases
# print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    '''
    for every letter that is guessed
      remove the letter from the availible letters
    return letters availible
    '''
    import string
    letter_list = list(string.ascii_lowercase)
    letter_remain = ""
    

    for letter in letters_guessed:
      letter_list.remove(letter)
    for element in letter_list:
      letter_remain += element
    return letter_remain

      



#Testcases 
# print( get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) )
  
def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print ("The secret word has ", len(secret_word), ' letters')
    print("Good luck!")
    lives_remain = 8
    letters_guessed = []
    while lives_remain > 0:
      print("You have", lives_remain, "lives")
      print("letters remaining : ", get_available_letters(letters_guessed))
      current_guess = input("Guess a letter: " ).lower()
      if current_guess in letters_guessed:
        print("You already guessed this letter!:", get_guessed_word(secret_word, letters_guessed))
      else:
        letters_guessed.append(current_guess)
        if current_guess in secret_word:
          print("correct :",get_guessed_word(secret_word, letters_guessed))
        else:
          lives_remain -= 1
          print("incorrect : ",get_guessed_word(secret_word, letters_guessed))
      print("")
      if is_word_guessed(secret_word, letters_guessed) == True:
        return print("You win!, the secret word is :", secret_word)
    if is_word_guessed(secret_word, letters_guessed) == False:
        return print("Game over!, the secret word is :", secret_word)
      



def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()