"""
Given:
An array of integers between 1 and n, inclusive, where n is the length
of the array..

Return:
The first integer in the array that appears more than once. If no integers
enter more than once, return -1.
"""

# Inputs
array = [2, 1, 5, 2, 3, 3, 4]


# Solution #1
def firstDuplicateValue1(array: list) -> int:
    """
    Create a set to keep tack of the elements found in the input array.
    Return with the first element found twice, else return -1.

    time: O(n)
    space: O(n)
    """

    elements = set()
    for num in array:
        if num in elements:
            return num
        else:
            elements.add(num)

    return -1


# Solution #2
def firstDuplicateValue(array: list) -> int:
    """
    For each element in the array, check the array at the index of element -1.
    IF it is below 0, return the element, otherwise multiply the value at index
    element -1 by -1.

    Can be done because we know values will be 1-n where n is length of the array.
    This property allows us to cache if we found an element by turning the value at
    n-1 index into a negative value at the first pass through.

    time: O(n)
    space: O(1) -> not storing anything, altering array in place
    """

    for num in array:
        absNUm = abs(num)
        if array[absNUm - 1] < 0:
            return absNUm
        array[absNUm - 1] *= -1

    return -1
