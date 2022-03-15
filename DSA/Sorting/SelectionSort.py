"""
Given:
An array of integers.
Returns:
A sorted version of the array, using the selection sort algorithm.
"""
# Inputs
array = [8, 5, 2, 9, 5, 6, 3]

# Solution #1
def selectionSort(array: list) -> list:
    """
    Loop through the array. At each index, check every element at and after the
    current index, find the index of the smallest element. Swap the element with
    the smallest element with the element at the current index.

    time: O(n^2) -> looping multiple times every index
    space: O(1) -> all work done in place
    """

    for i in range(len(array)):
        smallestIdx = None
        for j in range(i, len(array)):
            if smallestIdx is None or array[j] < array[smallestIdx]:
                smallestIdx = j
        array[i], array[smallestIdx] = array[smallestIdx], array[i]

    return array
