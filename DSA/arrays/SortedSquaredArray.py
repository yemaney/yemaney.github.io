"""
Write a function that take in a non-empty array of integers that
are sorted in ascending order.

Return a new array of the same length with squares of the input array
also sorted in ascending order.

Example: [1,2,3] -> [1,4,9]
"""

# Inputs
array = [-7, -3, 1, 9, 22, 30]

#   solution #1
def sortedSquaredArray1(array: list) -> list:
    """
    Square each element in the array. Then  sort it.

    time: O(nlogn) -> due to sorting
    space: O(n) -> storing array the length of input
    """
    squaredArray = [num ** 2 for num in array]
    squaredArray.sort()
    return squaredArray


# Solution #2
def sortedSquaredArray2(array: list) -> list:
    """
    Create pointers for rightmost and leftmost elements in the array, and
    an empty array of the same length as the input array.

    Compare absolute of elements at pointers. Put the larger one's square
    at the end of the empty array. If right > left, decrement right. I left > right,
    increment left.

    time: O(n) time -> traversing array once
    space: O(n) time -> creating new array of same length
    """

    newArray = [_ for _ in array]
    left = 0
    right = len(newArray) - 1

    for idx in reversed(range(len(array))):
        if abs(array[left]) > abs(array[right]):
            newArray[idx] = array[left] ** 2
            left += 1
        else:
            newArray[idx] = array[right] ** 2
            right -= 1

    return newArray
