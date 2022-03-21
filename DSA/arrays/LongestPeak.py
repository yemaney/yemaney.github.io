"""
Given:
A array of integers.

Return:
The length of the longest peak. A peak is defined as adjacent integers
that are strictly increasing, until a peak, and then strictly decreasing.

Ex) 1 2 3 0
"""

# Inputs
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

# Solution #1
def longestPeak1(array: list) -> int:
    """
    Traverse array from left to right. If an upward slope, a peak, and a downward
    slope are found in order record lengths. Return max length found.

    time: O(n) -> traversing entire array
    space: O(1) -> only storing pointers and length int
    """

    peakLength = 0

    for i in range(len(array) - 2):
        start = i
        currentLength = 1
        upSlope, downSlope = False, False

        while array[start] < array[start + 1]:
            upSlope = True
            start += 1
            currentLength += 1
            if start + 1 == len(array):
                break

        if start + 1 == len(array) or currentLength < 2:
            continue

        while array[start] > array[start + 1]:
            downSlope = True
            start += 1
            currentLength += 1
            if start + 1 == len(array):
                break

        if currentLength >= 3 and currentLength > peakLength and upSlope and downSlope:
            peakLength = currentLength

    return peakLength


# Solution #2
def longestPeak2(array: list) -> int:
    """
    Traverse array until reaching a peak. Check peaks length. Update longest
    peak length when appropriate. Return the longest peak length.

    time: O(n) -> traversing entire array
    space: O(1) -> only storing pointers and length int
    """

    longestPeakLength = 0
    i = 1

    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1

        right = i + 2
        while right < len(array) and array[right] < array[right - 1]:
            right += 1

        currentLength = right - left - 1
        longestPeakLength = max(currentLength, longestPeakLength)
        i = right

    return longestPeakLength
