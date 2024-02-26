"""
Given:
A string of lowercase english letters.

Return:
The index of the string's first non repeating character. If the input
string doesn't have a non repeating character, return -1.
"""

# Inputs #1
string = "abcdcaf"


# Solution #1
def firstNonRepeatingCharacter(string: str) -> int:
    """
    Create a dictionary of character counts in string. Then iterate
    over letters in string, in order, return strings index if its
    count is 1.

    time: O(n) -> iterating over string twice
    space: O(1) -> hash table is limited to lowercase english letters
    """

    characterCounts = {}

    for character in string:
        if character not in characterCounts:
            characterCounts[character] = 0
        characterCounts[character] += 1

    for idx, character in enumerate(string):
        if characterCounts[character] == 1:
            return idx

    return -1
