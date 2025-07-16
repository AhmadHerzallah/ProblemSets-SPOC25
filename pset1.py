# ================================================================
# Problem Set 1 (Problems 1, 2, 3)
# Students: Only edit the code in the indicated "solution_*" functions.
# Do NOT change the function signatures. Do NOT modify any code below
# the sentinel lines that say "DON'T WRITE ANYTHING BELOW THIS LINE".
# ================================================================

# ----------------------------------------------------------------
# Problem 1: Count Vowels
# ----------------------------------------------------------------
def solution_p1_vowels(s):
    """
    Count the number of vowels in the given lowercase string `s`.

    Parameters
    ----------
    s : str
        Input string consisting of lowercase characters (other chars like spaces
        may appear in some tests—just ignore anything not a vowel).

    Returns
    -------
    int
        Number of vowels in `s`. Valid vowels: 'a', 'e', 'i', 'o', 'u'.

    Example
    -------
    s = 'azcbobobegghakl' -> 5
    """
    # TODO: Implement vowel counting.
    # Hint: iterate through characters and check membership in "aeiou".
    vowel_count = 0 # placeholder; replace with your code
    return vowel_count

""" DON'T WRITE ANYTHING BELOW THIS LINE (Problem 1 tests) """
def _test_problem1():
    test_cases = [
        ('azcbobobegghakl', 5),  # provided example
        ('hello', 2),
        ('world', 1),
        ('python', 1),
        ('aeiou', 5),
        ('xyz', 0),
        ('', 0),
        ('a quick brown fox jumps over the lazy dog', 11),
    ]

    print("=== Testing Problem 1: Count Vowels ===")
    for i, (inp, expected) in enumerate(test_cases, start=1):
        result = solution_p1_vowels(inp)
        assert result == expected, (
            f"Problem 1 Test {i} failed: expected {expected}, got {result}"
        )
        print(f'Problem 1 Test {i} passed: "{inp}" -> {result} vowels.')
    print()

# ----------------------------------------------------------------
# Problem 2: Count occurrences of "bob" (allow overlaps)
# ----------------------------------------------------------------
def solution_p2_bob(s):
    """
    Count the number of times the substring 'bob' occurs in the given lowercase
    string `s`. Overlapping occurrences count.

    Parameters
    ----------
    s : str
        Input string consisting of lowercase characters.

    Returns
    -------
    int
        Number of (possibly overlapping) occurrences of the substring 'bob'.

    Examples
    --------
    'azcbobobegghakl' -> 2
    'bobob' -> 2  (positions 0-2 and 2-4 overlap)
    """
    # TODO: Implement overlapping substring count.
    # Hint: slide a window of length 3 across s and compare to "bob".
    bob_count = 0 # placeholder; replace with your code
    return bob_count

""" DON'T WRITE ANYTHING BELOW THIS LINE (Problem 2 tests) """
def _test_problem2():
    test_cases = [
        ('azcbobobegghakl', 2),  # provided example
        ('bob', 1),
        ('bobob', 2),            # overlap check
        ('bobby', 1),
        ('bbbb', 0),
        ('', 0),
    ]

    print("=== Testing Problem 2: Count 'bob' Occurrences ===")
    for i, (inp, expected) in enumerate(test_cases, start=1):
        result = solution_p2_bob(inp)
        assert result == expected, (
            f"Problem 2 Test {i} failed: expected {expected}, got {result}"
        )
        print(f'Problem 2 Test {i} passed: "{inp}" -> {result} occurrences of "bob".')
    print()

# ----------------------------------------------------------------
# Problem 3: Longest Alphabetical Substring
# ----------------------------------------------------------------
def solution_p3_longest_alpha(s):
    """
    Return the longest substring of `s` in which the letters appear in
    non-decreasing alphabetical order (i.e., each char >= previous char).
    In case of ties, return the *first* such longest substring.

    Parameters
    ----------
    s : str
        Input string of lowercase characters.

    Returns
    -------
    str
        The longest alphabetical-order substring (first one if tie).
        For an empty input string, return ''.

    Examples
    --------
    'azcbobobegghakl' -> 'beggh'
    'abcbcd'          -> 'abc'  (tie broken by first longest)
    """
    # TODO: Implement longest alphabetical substring search.
    # Typical approach: track `current` run and `longest` run as you scan.
    if not s:  # placeholder scaffold; replace with full implementation
        return ""
    longest = s[0] # placeholder
    return longest

""" DON'T WRITE ANYTHING BELOW THIS LINE (Problem 3 tests) """
def _test_problem3():
    test_cases = [
        ('azcbobobegghakl', 'beggh'), # provided example
        ('abcbcd', 'abc'),            # provided example (tie -> first)
        ('aaaaa', 'aaaaa'),
        ('zyx', 'z'),                 # descending -> first char
        ('', ''),                     # empty
        ('abcabcabc', 'abc'),         # repeats
    ]

    print("=== Testing Problem 3: Longest Alphabetical Substring ===")
    for i, (inp, expected) in enumerate(test_cases, start=1):
        result = solution_p3_longest_alpha(inp)
        assert result == expected, (
            f"Problem 3 Test {i} failed: expected '{expected}', got '{result}'"
        )
        print(f'Problem 3 Test {i} passed: "{inp}" -> "{result}".')
    print()

# ----------------------------------------------------------------
# Master test runner
# ----------------------------------------------------------------
def main():
    _test_problem1()
    _test_problem2()
    _test_problem3()

if __name__ == "__main__":
    main()
# ================================================================