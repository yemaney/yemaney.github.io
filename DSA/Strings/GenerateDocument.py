"""
Given:
A string of available characters, and a string representing a document.

Return:
A boolean representing whether the document can be created using the
provided characters.
"""

# Inputs
characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

# Solution #1
def generateDocument(characters: str, document: str) -> bool:
    """
    Create a dictionary of character counts available. Loop through
    each character in the document, and decrement its count from
    characterCounts. If a character from document is not available,
    return False.

    time: O(n + m) -> where n is number of characters, m is length if document
    space: O(c) -> where c is number of unique characters in characters
    """

    characterCounts = {}

    for character in characters:
        if character not in characterCounts:
            characterCounts[character] = 0
        characterCounts[character] += 1

    for character in document:
        if character not in characterCounts or characterCounts[character] == 0:
            return False
        characterCounts[character] -= 1
    return True
