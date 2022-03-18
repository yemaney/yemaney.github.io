"""
Given:
An array of integers and an integer.

Return:
Move all the instances of the input integer to the end of the array, 
in place and return the array itself.
"""

# Inputs
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

# Solution #1
def moveElementToEnd(array: list, toMove: int) -> list:
    """
    Create right and left pointers. Decrement right pointer if
    element at its index is toMove, increment left pointer if
    element at index is not toMove. Swap elements if left element
    is toMove and right element is not toMove.

    time: O(n) -> traversing entire array once
    space: O(1) -> all changes happening in place
    """

    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] != toMove:
            left += 1
        else:
            if array[right] != toMove:
                array[left], array[right] = array[right], array[left]
                left += 1
            right -= 1

    return array
