"""
Given:
An array of positive integers.

Return:
The maximum sum of non-adjacent elements in the array. If the input array
is empty, return 0.
"""

# Inputs
array = [75, 105, 120, 75, 90, 135]


# Solution 1
def maxSubsetSumNoAdjacent1(array: list) -> int:
    """
    Iterate over each index i in the input array. At each iteration calculate
    the max subset sum with no adjacent elements up until i, and append to a
    sumArray. Return the last element in the sumArray.
    This takes advantage of the fact that at index i, the max subset sum is
    either the same as the max subset at index i-1, or max subset at i-2 + i.


    time: O(n) Traversing through entire array
    space: O(n) creating an new sumArray of same size as the input array
    """
    if array == []:
        return 0

    sumArray = []
    for i in range(len(array)):
        if i == 0:
            maxSum = array[i]
        elif i == 1:
            maxSum = max(array[i - 1], array[i])
        else:
            first = sumArray[i - 2]
            second = sumArray[i - 1]
            maxSum = max(second, first + array[i])

        sumArray.append(maxSum)
    return sumArray[-1]


# Solution 2
def maxSubsetSumNoAdjacent2(array: list) -> int:
    """
    This takes advantage of the fact that at index i, the max subset sum is
    either the same as the max subset at index i-1, or max subset at i-2 + i.
    Save space by only keepting track of max subset sums at i and i - 2.

    time: O(n) Traversing through entire array
    space: O(1) Only keeping track of two values
    """

    if array == []:
        return 0

    lastMax, currentMax = 0, 0
    for i in range(len(array)):
        if i == 0:
            currentMax = array[i]
        elif i == 1:
            lastMax, currentMax = currentMax, max(array[i - 1], array[i])
        else:
            lastMax, currentMax = currentMax, max(currentMax, lastMax + array[i])
    return currentMax
