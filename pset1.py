def solution(s):
    """
    Function to count the number of vowels in a given string.
    """
    # Initialize a counter for vowels
    vowels = "aeiou"  # Define valid vowels

    # Write a for loop that iterates through each character in the string s
    # Increase vowel_count by 1 for each vowel found
    # Return the total count of vowels

""" DON'T WRITE ANYTHING BELOW THIS LINE """
def main():
    # Test cases
    test_cases = [
        ('azcbobobegghakl', 5),
        ('hello', 2),
        ('world', 1),
        ('python', 1),
        ('aeiou', 5),
        ('xyz', 0),
        ('', 0),
        ('a quick brown fox jumps over the lazy dog', 11),
        ('', 0),
    ]
    for i, (input_str, expected_count) in enumerate(test_cases):
        result = solution(input_str)  # Call solution with the input string
        assert result == expected_count, f'Test case {i + 1} failed: expected {expected_count}, got {result}'
        print(f'Test case {i + 1} passed: "{input_str}" has {result} vowels.')

if __name__ == "__main__":
    main()
""" DON'T WRITE ANYTHING ABOVE THIS LINE """