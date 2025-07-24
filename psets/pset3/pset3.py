# ================================================================
# Problem Set 3: Hangman
# Students: Only edit the code in the indicated solution functions (with TODOs).
# DO NOT change function signatures. DO NOT modify any code below the
# sentinel lines that say "DON'T WRITE ANYTHING BELOW THIS LINE".
# ================================================================

import string
import random

# ----------------------------------------------------------------
# Problem 1: isWordGuessed
# ----------------------------------------------------------------
def isWordGuessed(secretWord, lettersGuessed):
    """
    Return True if *every* letter of secretWord appears in lettersGuessed;
    otherwise return False.

    Parameters
    ----------
    secretWord : str
        The word the player is trying to guess (all lowercase letters).
    lettersGuessed : list[str]
        Letters guessed so far (all lowercase, may contain duplicates).

    Returns
    -------
    bool
    """
    # TODO: Return True only if all letters in secretWord are in lettersGuessed.
    return False # placeholder

""" DON'T WRITE ANYTHING BELOW THIS LINE (Problem 1 tests) """
def _test_problem1():
    cases = [
        ('apple', ['e','i','k','p','r','s'], False),
        ('apple', ['a','p','l','e'], True),
        ('else',  ['e','l','s'], True),
        ('else',  ['e','l'], False),
        ('else',  ['e','l','s','x','y','z','e'], True),
        ('',      [], True),  # empty secret trivially guessed
    ]
    print("=== Testing Problem 1: isWordGuessed ===")
    for i,(w,lg,exp) in enumerate(cases,1):
        got = isWordGuessed(w, lg)
        assert got == exp, f"Problem 1 Test {i} failed: expected {exp}, got {got}"
        print(f"Problem 1 Test {i} passed: secretWord='{w}', lettersGuessed={lg} -> {got}")
    print()

# ----------------------------------------------------------------
# Problem 2: getGuessedWord
# ----------------------------------------------------------------
def getGuessedWord(secretWord, lettersGuessed):
    """
    Return a string showing which letters in secretWord have been guessed.

    Revealed letters appear in place; unknown letters shown as '_ ' (underscore
    plus trailing space for readability). Spacing is not graded strictly by most
    autograders, but we use a single space after underscores.

    Example:
        secretWord='apple', lettersGuessed=['e','i','k','p','r','s']
        returns '_ pp_ e'
    """
    # TODO: Build and return the masked string as described above.
    return "_ " * len(secretWord) # placeholder

""" DON'T WRITE ANYTHING BELOW THIS LINE (Problem 2 tests) """
def _norm_mask(s):
    """
    Helper for tests: normalize masks by stripping spaces so spacing differences
    don't cause false negatives in student code. Letters are preserved.
    """
    return s.replace(' ', '')

def _expected_mask(secretWord, lettersGuessed):
    return ''.join(ch if ch in lettersGuessed else '_' for ch in secretWord)

def _test_problem2():
    cases = [
        ('apple', ['e','i','k','p','r','s'], '_pp_e'),
        ('apple', list('apple'), 'apple'),
        ('else',  list('e'), 'e__e'),
        ('banana', list('an'), 'banana'.replace('b','_').replace('a','a').replace('n','n')),
        ('', [], ''),
    ]
    print("=== Testing Problem 2: getGuessedWord ===")
    for i,(w,lg,exp_mask) in enumerate(cases,1):
        got = getGuessedWord(w, lg)
        if got is None:
            raise AssertionError(f"Problem 2 Test {i} failed: function returned None.")
        # compare normalized
        assert _norm_mask(got) == exp_mask, (
            f"Problem 2 Test {i} failed:\n"
            f"  secretWord='{w}', lettersGuessed={lg}\n"
            f"  expected mask (spaces ignored): '{exp_mask}'\n"
            f"  got: '{got}'"
        )
        print(f"Problem 2 Test {i} passed: '{w}' -> '{got}'")
    print()

# ----------------------------------------------------------------
# Problem 3: getAvailableLetters
# ----------------------------------------------------------------
def getAvailableLetters(lettersGuessed):
    """
    Return a string of lowercase letters (a-z) *not yet guessed*.

    Letters appear in alphabetical order (standard ASCII lowercase order).
    """
    # TODO: Return remaining letters not in lettersGuessed.
    return string.ascii_lowercase # placeholder

""" DON'T WRITE ANYTHING BELOW THIS LINE (Problem 3 tests) """
def _test_problem3():
    cases = [
        (['e','i','k','p','r','s'], "abcdfghjlmnoqtuvwxyz"),
        ([], string.ascii_lowercase),
        (list('abcdefghijklmnopqrstuvwxyz'), ""),
        (['a','b','c','a'], string.ascii_lowercase[3:]),
    ]
    print("=== Testing Problem 3: getAvailableLetters ===")
    for i,(lg,exp) in enumerate(cases,1):
        got = getAvailableLetters(lg)
        assert got == exp, (
            f"Problem 3 Test {i} failed:\n"
            f"  lettersGuessed={lg}\n"
            f"  expected '{exp}'\n"
            f"  got '{got}'"
        )
        print(f"Problem 3 Test {i} passed: lettersGuessed={lg} -> '{got}'")
    print()

# ----------------------------------------------------------------
# Problem 4: hangman game (interactive)
# ----------------------------------------------------------------
def hangman(secretWord):
    """
    Play an interactive game of Hangman with the user guessing letters.

    Rules
    -----
    * User starts with 8 guesses.
    * Repeated guesses do NOT cost a guess; show message.
    * Incorrect *new* guesses decrement remaining guesses.
    * Show current guessed word and available letters after each round.
    * End when word guessed (win) or guesses reach 0 (lose).
    * All comparisons lowercase; convert user input with .lower().
    * Accept only single alphabetic characters; ignore/reprompt otherwise.

    This function PRINTS the game transcript and returns None.
    """
    # TODO: Implement the interactive game using your helper functions above.
    # Recommended variable names (as used in the spec):
    #   guessesLeft = 8
    #   lettersGuessed = []
    # Use isWordGuessed / getGuessedWord / getAvailableLetters
    # for consistency with student-implemented helpers.
    #
    # Remember: do NOT print the result of calling this function (it returns None).
    #
    # Placeholder scaffold:
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secretWord)} letters long.")
    print("-------------")
    print("(hangman game not yet implemented)")
    return

# ----------------------------------------------------------------
# Wordlist loading utilities (safe fallbacks for local testing)
# ----------------------------------------------------------------
_WORDLIST_DEFAULT = ["apple", "banana", "grape", "tact", "else", "orange", "pear", "melon"]

def loadWords(filename="words.txt"):
    """
    Try to load a list of lowercase words (space or newline separated) from
    `filename`. If the file cannot be read, fall back to a small built-in list.
    """
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

def chooseWord(wordlist):
    """Return a random word from `wordlist`."""
    return random.choice(wordlist)

# ----------------------------------------------------------------
# Optional demo runner (interactive) -- NOT used in grading tests
# ----------------------------------------------------------------
def play_hangman_demo():
    """
    Load words (or fallback) and play one interactive game.
    Safe to run locally; NOT invoked by automated tests.
    """
    wordlist = loadWords()
    secretWord = chooseWord(wordlist)
    hangman(secretWord)

# ----------------------------------------------------------------
# Master test runner (Problems 1–3 only; no interactive I/O)
# ----------------------------------------------------------------
def main():
    _test_problem1()
    _test_problem2()
    _test_problem3()
    print("Helper functions look good! To play interactively, call play_hangman_demo().")

if __name__ == "__main__":
    main()
# ================================================================
