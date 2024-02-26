"""
Given : 
A non empty array of integers.

Returns : 
The maximum sum that can be obtained by summing up integers in a non empty
sub array of the input array.
"""

from __future__ import annotations

# Inputs
array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

# Solution
def kadanesAlgo(array: list[int]) -> int:
    """
    Uses dynamic programming. Start with first integer being the maxSum. Then
    progressively consider the next integers in the array. The max sum possible
    at any position in the array is either the value it holds or the sum of all
    its predecessors with its value.

    time: O(n) -> looping entire array
    space: O(1) -> only storing maxSum int, plus altering original array
    """

    maxSum = array[0]

    for i in range(1, len(array)):
        array[i] = max(array[i], array[i] + array[i - 1])
        maxSum = max(maxSum, array[i])
    return maxSum
