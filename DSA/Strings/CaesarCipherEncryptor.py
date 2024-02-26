"""
Given:
A non-empty string of lowercase letters, and a non-negative integer (key).

Return:
A new string obtained by shifting every letter in the input string by
key position in the alphabet. The alphabet is "wrapped", the letter 
after z is a.
"""
# Inputs
string = "xyz"
key = 2

# Solution #1
def caesarCipherEncryptor(string: str, key: int) -> str:
    """
    Loop thorugh each letter in the string. Use modulus to find correct
    index after shifting current letter indexes by key. Append new letter
    to a list, and finally return a string by joining the list.

    time: O(n) -> traversing over every letter of the string
    space: O(n) -> constructing a new string of same length as original
    """

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    encrypted = []
    for letter in string:
        newIdx = (alphabet.index(letter) + key) % 26
        encrypted.append(alphabet[newIdx])

    return "".join(encrypted)
