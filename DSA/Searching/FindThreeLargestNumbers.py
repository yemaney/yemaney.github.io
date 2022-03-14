"""
Given:
An array of at least three integers.

Return:
Without sorting the input array, return a sorted array of the three
largest integers in the input array. Duplicated allowed.

Example:
[10, 5, 9, 10, 12] -> [10, 10, 12]
"""

# Input
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

# Solution #1
def findThreeLargestNumbers(array: list) -> list:
    """
    Create an array (threeLargest) of three None values. For each element of
    the array check if it is larger than one of current threeLargest in the order
    of largest to smallest. Update the array, and shift it's elements accordingly.


    time: O(n) -> traversing through all elements of the array passed
    space: O(1) -> storing and updating a 3 element array, it doesn't grow
    """

    threeLargest = [None, None, None]

    for num in array:
        if threeLargest[2] is None or num > threeLargest[2]:
            idx = 2
        elif threeLargest[1] is None or num > threeLargest[1]:
            idx = 1
        elif threeLargest[0] is None or num > threeLargest[0]:
            idx = 0
        else:
            continue
        shiftUpdate(threeLargest, num, idx)

    return threeLargest


def shiftUpdate(threeLargest: list, num: int, idx: int) -> None:
    for i in range(idx + 1):
        if i == idx:
            threeLargest[idx] = num
        else:
            threeLargest[i] = threeLargest[i + 1]
