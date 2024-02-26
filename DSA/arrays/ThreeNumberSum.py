"""
Given:
An array of unique integers and an interger reperesenting a target sum.

Return:
An array of all triplets in the input array that sum up to the target.
"""

# Inputs
array = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0

# Solution #1
def threeNumberSum1(array: list, targetSum: int) -> list:
    """
    Use three for loops to find any triplets that sum up to the target.

    time: O(n^3) -> Three loops
    space: O(n) -> number of triplets scales with array size
    """

    triplets = []

    for i in range(len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array)):
                print(i, j, k)
                if array[i] + array[j] + array[k] == targetSum:
                    triplets.append([array[i], array[j], array[k]])

    return triplets


# Solution #2
def threeNumberSum2(array: list, targetSum: int) -> list:
    """
    Sort the input array. Loop thorugh n-2 elements of the array. Use
    left and right pointers at each loop, to discover any possible two
    numbers that, along with the current number, sum up to the target.

    time: O(n^2) -> Looping twice thorugh array (for + while)
    space: O(n^2) -> number of triplets scales with array size
    """

    array.sort()

    triplets = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        print(i)
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum > targetSum:
                right -= 1
            elif currentSum < targetSum:
                left += 1
            else:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1

    return triplets
