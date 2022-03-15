"""
Given:
A non empty string.

Return:
A boolean indicating whetether the string is a palindrome or not. A 
palindrome is a string that's written the same forward and backward.
"""
# Inputs
string = "abcdcba"

# Solution#1
def isPalindrome(string: str) -> bool:
    """
    Create pointers for left and right ends of string. Check if letters
    at pointers are the same, if not return False. If they are equal,
    increment the pointer index accordingly, and perform the check again,
    so long as the right pointer is larger than the left pointer.

    time: O(n) -> will loop at most 1/2n times
    space: O(1) -> only storing pointers
    """

    left = 0
    right = len(string) - 1

    while right > left:
        if string[right] != string[left]:
            return False
        left += 1
        right -= 1

    return True
