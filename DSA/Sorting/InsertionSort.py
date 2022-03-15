"""
Given:
An array of integers.
Returns:
A sorted version of the array, using the insertion sort algorithm.
"""
# Inputs
array = [8, 5, 2, 9, 5, 6, 3]

# Solution #1
def insertionSort(array: list) -> list:
    """
    Loop through each element of the array and while the element is
    less than the one before it, swap the elements.
    time: O(n^2) -> looping through array for each element
    space: O(1) -> all operations are in place
    """
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array
