"""
Given:
A sorted array of integers as well as a target integer.

Return:
Write a function that implements the binary search algorithm to 
determin if the target integer is contained in the array. If it is
return it's index, else return -1.
"""
# Inputs
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

# Solution #1
def binarySearch(array: list, target: int) -> int:
    """
    Create pointers for the leftmost, rightmost, and middle element
    indexes of the array. Compare target integer with the middle
    element. Adjust the pointers accordingly.

    time: O(lloh(n)) -> will be removing half the array elements each iteration
    space: O(1) -> not really storing anything that grows
    """

    left = 0
    right = len(array) - 1
    middle = (left + right) // 2

    while array[middle] != target:
        print(middle)
        if left > right:
            return -1
        if array[middle] > target:
            right = middle - 1
        elif array[middle] < target:
            left = middle + 1
        middle = (left + right) // 2

    return middle
