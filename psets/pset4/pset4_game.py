# ================================================================
# Problem Set 4: Word Game
#
# This module implements the Word Game itself, and allows it to be played against a human
#
# Students: Only edit the code in the indicated solution functions (with TODOs).
# DO NOT change function signatures. DO NOT modify any code below the
# sentinel lines that say "DON'T WRITE ANYTHING BELOW THIS LINE".
# ================================================================

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

WORDLIST_FILENAME = "words.txt"

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# -----------------------------------

_WORDLIST_DEFAULT = ["apple", "banana", "grape", "tact", "else", "orange", "pear", "melon"]
def loadWords(filename=WORDLIST_FILENAME):
    """
    Try to load a list of lowercase words (space or newline separated) from
    `filename`. If the file cannot be read, fall back to a small built-in list.
    """
    print("Loading word list from file...")
    try:
        with open(filename, "r") as f:
            content = f.read()
        words = content.split()
        words = [w.strip().lower() for w in words if w.strip()]
        if words:
            print("Loading word list from file...")
            print(f"{len(words)} words loaded.")
            return words
    except OSError:
        pass
    # fallback
    print("Loading fallback word list...")
    print(f"{len(_WORDLIST_DEFAULT)} words loaded.")
    return list(_WORDLIST_DEFAULT)

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# ----------------------------------------------------------------
# Problem #1: Scoring a word
# ----------------------------------------------------------------
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TODO ... <-- Remove this comment when you code this function
    assert False, 'getWordScore is unimplemented!' # <-- Remove this line when you code the function
    return 0


# ----------------------------------------------------------------
# Problem #2: Dealing with Hands
# ----------------------------------------------------------------

# This function is complete (DO NOT CHANGE)
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                              # print an empty line

# This function is complete (DO NOT CHANGE)
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

# Update a hand by removing letters
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TODO
    assert False, 'updateHand is unimplemented!' # <-- Remove this line when you code the function
    return {}


# ----------------------------------------------------------------
# Problem #3: Test word validity
# ----------------------------------------------------------------
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TODO
    assert False, 'isValidWord is unimplemented!' # <-- Remove this line when you code the function
    return False

# ----------------------------------------------------------------
# Problem #4: Test word validity
# ----------------------------------------------------------------
def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    # TODO
    assert False, 'calculateHandlen is unimplemented!' # <-- Remove this line when you code the function
    return 0

# ----------------------------------------------------------------
# Problem #5: Playing a Hand
# ----------------------------------------------------------------
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score

    # As long as there are still letters left in the hand:

        # Display the hand

        # Ask user for input

        # If the input is a single period:

            # End the game (break out of the loop)


        # Otherwise (the input is not a single period):

            # If the word is not valid:

                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line

                # Update the hand


    # Game is over (user entered a '.' or ran out of letters), so tell user the total score


# ----------------------------------------------------------------
# Problem #6: Playing a Game
# ----------------------------------------------------------------
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    # TODO
    assert False, 'playGame is unimplemented!' # <-- Remove this line when you code the function



# DO NOT WRITE ANYTHING BELOW THIS LINE
# Test code
# You don't need to understand how this test code works (but feel free to look it over!)

def test_getWordScore():
    """
    Unit test for getWordScore
    """
    failure=False
    # dictionary of words and scores
    words = {
            ("", 7) : 0,
			("it", 7) : 4,
			("was", 7) : 18,
			("scored", 7) : 54,
			("waybill", 7) : 155,
			("outgnaw", 7) : 127,
			("fork", 7) : 44,
			("fork", 4) : 94
    }
    for (word, n) in words.keys():
        score = getWordScore(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_getWordScore()")
            print("\tExpected", words[(word, n)], "points but got '" + str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True
    if not failure:
        print("SUCCESS: test_getWordScore()")

def test_updateHand():
    """
    Unit test for updateHand
    """
    # test 1
    handOrig = {'a' : 1, 'q' : 1, 'l' : 2, 'm' : 1, 'u' : 1, 'i' : 1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'l' : 1, 'm' : 1}
    expectedHand2 = {'a' : 0, 'q' : 0, 'l' : 1, 'm' : 1, 'u' : 0, 'i' : 0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

        return # exit function
    if handCopy != handOrig:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)

        return # exit function

    # test 2
    handOrig = {'e' : 1, 'v' : 2, 'n' : 1, 'i' : 1, 'l' : 2}
    handCopy = handOrig.copy()
    word = "evil"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'v' : 1, 'n':1, 'l':1}
    expectedHand2 = {'e' : 0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)

        return # exit function

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "hello"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {}
    expectedHand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)

        return # exit function

    print("SUCCESS: test_updateHand()")

# end of test_updateHand

def test_isValidWord(wordList):
    """
    Unit test for isValidWord
    """
    failure=False
    # test 1
    word = "hello"
    handOrig = getFrequencyDict(word)
    handCopy = handOrig.copy()

    if not isValidWord(word, handCopy, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", handOrig)

        failure = True

    # Test a second time to see if wordList or hand has been modified
    if not isValidWord(word, handCopy, wordList):
        print("FAILURE: test_isValidWord()")

        if handCopy != handOrig:
            print("\tTesting word", word, "for a second time - be sure you're not modifying hand.")
            print("\tAt this point, hand ought to be", handOrig, "but it is", handCopy)

        else:
            print("\tTesting word", word, "for a second time - have you modified wordList?")
            wordInWL = word in wordList
            print("The word", word, "should be in wordList - is it?", wordInWL)

        print("\tExpected True, but got False for word: '" + word + "' and hand:", handCopy)

        failure = True


    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "rapture"

    if  isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "evil"

    if  not isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 6
    word = "even"

    if  isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, make sure isValidWord() isn't mutating its inputs)")

        failure = True

    if not failure:
        print("SUCCESS: test_isValidWord()")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    print("----------------------------------------------------------------------")
    print("Testing getWordScore...")
    test_getWordScore()
    print("----------------------------------------------------------------------")
    print("Testing updateHand...")
    test_updateHand()
    print("----------------------------------------------------------------------")
    print("Testing isValidWord...")
    test_isValidWord(wordList)
    print("----------------------------------------------------------------------")
    print("All done! --- opening game")
    playGame(wordList)
