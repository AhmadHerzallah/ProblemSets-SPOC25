def solution(s):
    """
    Function to count the number of vowels in a given string.

    Parameters:
    s : str : The input string consisting of lowercase characters.

    Returns:
    int : The number of vowels in the input string.
    """
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Define valid vowels
    vowels = "aeiou"
    
    # TODO: Implement your code to count the vowels in the string s
    # Iterate through each character in s
    # If the character is a vowel, increment vowel_count
    
    # Return the total count of vowels
    return vowel_count

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
    ]
    
    for i, (input_str, expected_count) in enumerate(test_cases):
        result = solution(input_str)  # Call the solution function with the input string
        assert result == expected_count, f'Test case {i + 1} failed: expected {expected_count}, got {result}'
        print(f'Test case {i + 1} passed: "{input_str}" has {result} vowels.')

if __name__ == "__main__":
    main()
""" DON'T WRITE ANYTHING ABOVE THIS LINE """