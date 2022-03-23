"""
Given:
A array of arbitrary intervals.

Return:
Merge any overlapping intervals,

Example) [1, 4] and [4, 6] are overlapping intervals
"""
# Inputs
from typing import List

intervals = [
    [1, 10],
    [10, 20],
    [20, 30],
    [30, 40],
    [40, 50],
    [50, 60],
    [60, 70],
    [70, 80],
    [80, 90],
    [90, 100],
]

# Solution #1
def mergeOverlappingIntervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Sort the interval array in order to compare their end values to deduce if they overlap.
    Loop over evert interval, if they overlap figure out the new current interval, else
    append to merged array.

    time: O(nlog(n))
    space: O(n)
    """

    intervals.sort()

    merged = []
    currentInterval = intervals[0]
    merged.append(currentInterval)

    for interval in intervals:
        currentStart, currentEnd = currentInterval
        nextStart, nextEnd = interval

        if currentEnd >= nextStart:
            currentInterval[0] = min(currentStart, nextStart)
            currentInterval[1] = max(currentEnd, nextEnd)
        else:
            currentInterval = interval
            merged.append(currentInterval)

    return merged
