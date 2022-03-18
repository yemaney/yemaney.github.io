"""
Given:
Two non empty arrays of integers.

Return:
A pair of integers, one of each coming from one the input arrays, that
have the smallest absolute difference in value.
"""

# Inputs
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

# Solution #1
def smallestDifference1(arrayOne: list, arrayTwo: list) -> list:
    """
    Loop through each list to find the smallest difference.

    time: O() ->
    space: O(1) -> only storing smallestDiff
    """

    smallestDiff = [arrayOne[0], arrayTwo[0]]
    for n1 in arrayOne:
        for n2 in arrayTwo:
            diff = abs(n1 - n2)
            if diff < abs(smallestDiff[0] - smallestDiff[1]):
                smallestDiff = [n1, n2]

    return smallestDiff


def smallestDifference(arrayOne: list, arrayTwo: list) -> list:
    """
    Sort both arrays, and create pointers to the begining of both
    sorted arrays. Move along both arrays and calculate the difference,
    updating the smallest difference and pointers appropriately.

    time: O(nlog(n)) + O(mlog(m)) -> sorting both arrays
    space: O(1) -> storing only pointers and a small list
    """

    arrayOne.sort()
    arrayTwo.sort()

    leftOne = 0
    leftTwo = 0

    smallestDifference = [arrayOne[leftOne], arrayTwo[leftTwo]]

    while leftOne < len(arrayOne) and leftTwo < len(arrayTwo):
        currentDifference = [arrayOne[leftOne], arrayTwo[leftTwo]]

        if difference(*currentDifference) < difference(*smallestDifference):
            smallestDifference = currentDifference

        if arrayOne[leftOne] < arrayTwo[leftTwo]:
            leftOne += 1
        elif arrayOne[leftOne] > arrayTwo[leftTwo]:
            leftTwo += 1
        else:
            return currentDifference

    return smallestDifference


def difference(a, b):
    return abs(a - b)
