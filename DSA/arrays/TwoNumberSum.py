"""
Write a function that takes in a non-empty array of distinc integers
and an integer representing a target sum.

If any two numbers in the input array sum up to the target sum, return
them in an array: [1, 2]
If no two numbers in the input array sum up to the target sum return
an empty array: []
"""

# Inputs
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

# Solution #1
def twoNumberSum1(array: list, targetSum: int) -> list:
    """
    Loop for each number in the input array, and the loop for each
    element after it.

    Check if the number sum to the targetSum.

    time: O(n^2) -> have to loop the array twice
    space: O(0) -> not storing anything
    """
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return []


# Solution #2
def twoNumberSum2(array: list, targetSum: int) -> list:
    """
    Create an empty dictionary.

    For each element in the array check if its compliment exists
    in the dictionary.

    If not put the element in the dictionary.

    time: O(n) time -> traverse the array only once
    space: O(n) space -> storing every element in the dictionary
    """

    nums = {}
    for num in array:
        compliment = targetSum - num
        if compliment in nums:
            return [compliment, num]
        else:
            nums[num] = True
    return []


# Solution #3
def twoNumberSum3(array: list, targetSum: int) -> list:
    """
    Sort the array.

    Check if the leftmost and rightmost elements of the array
    sum to the target.

    If the sum is less than the target, move the left pointer
    forward.
    If the sum is greater than the target, move the right pointer
    backward.

    time: O(nlogn)
    space: O(1) -> only storing pointers
    """
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1

    return []
