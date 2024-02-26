"""
Given:
An array of unsorted integers.

Return:
A sorted version of the unsorted array. Using the bubble sort algorithm.
"""

# Inputs
array = [8, 5, 2, 9, 5, 6, 3]

# Solution #1
def bubbleSort(array: list) -> list:
    """
    Iterate over the array, for each element check whether the next
    element is smaller, if so swap their positions. If a swap occurs
    during an iteration, repeat the cycle. Exit while loop if no swap
    occurs, during an iteration and return the array.

    time: O(n^2) -> maximum iteration of n^2 times
    space : O(1) -> not storing anything
    """

    while True:
        numOfSwaps = 0

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                numOfSwaps += 1

        if numOfSwaps == 0:
            return array
