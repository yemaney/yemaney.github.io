"""
Given:
An array of integers. Where each element represents a jump of indices in the array.

Return:
Whether the jumps in the array for a single cycle. A single cycle is when if you can
start at any index, and jump to every other index of the array once, and end up at the
initial index.
"""

from __future__ import annotations

# Inputs
array = [2, 3, 1, -4, -4, 2]


# Solution
def hasSingleCycle(array: list[int]) -> bool:
    """
    Start at index 0 and travel through the array. If the start index is visited
    again before number of visits is equal to len of array, early exist false.
    Else return the last index visited is 0.
    
    time: O(n) -> traversing entire array
    space: O(1) -> only keeping track of two integers
    """
    
    numVisits = 0
    currentIdx = 0
    while numVisits < len(array):
        if numVisits > 0 and currentIdx == 0:
            return False
        numVisits += 1
        currentIdx = (currentIdx + array[currentIdx]) % len(array)
        
    return currentIdx == 0
