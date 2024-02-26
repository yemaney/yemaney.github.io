"""
Given:
An array of integers.

Return:
A boolean value indicating whether the array is monotonic. An
array is monotonic if its elements from left to right are either
entirely non-increasing or monotonically non-decreasing.
"""

# Inputs
array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]

# Solution #1
def isMonotonic(array: list) -> bool:
    """
    Loop through array, decide "condition" the first time the change
    is not zero. Early exit and return False if the change ever goes
    against the established condition.

    time: O(n) -> looping through entire array
    space: O(1) -> only storing a pointer and condition flag
    """

    condition = None
    i = 1
    while i < len(array):
        if array[i] == array[i - 1]:
            pass
        elif array[i] > array[i - 1]:
            if condition is None:
                condition = "Non-Decreasing"
            elif condition != "Non-Decreasing":
                return False
        else:
            if condition is None:
                condition = "Non-Increasing"
            elif condition != "Non-Increasing":
                return False
        i += 1
    return True
