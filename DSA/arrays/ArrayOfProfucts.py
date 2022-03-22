"""
Given:
A non empty array of integers.

Return:
An array of same length as the input array. Where each element output is
equal to the product of every other number in the input array.
"""

# inputs
from itertools import product

array = [5, 1, 4, 2]

# Solution #1
def arrayOfProducts1(array: list) -> list:
    """
    Loop through the array, and calculate the product exclusive
    each element for each element.

    time: O(n^2)
    space: O(n)
    """

    aop = []

    i = 0
    while i < len(array):
        product = 1
        for j in range(len(array)):
            if j != i:
                product *= array[j]
        aop.append(product)
        i += 1
    return aop


# Solution #2
def arrayOfProducts2(array: list) -> list:
    """
    Create arrays to hold left and right products for each element in tbe
    input array. Then loop and multiply them together to get the array of
    products.

    time: O(n) -> 3 loops O(3n) -> O(n)
    space: O(n)
    """

    aop = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(leftProducts)):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    for i in range(len(array)):
        aop[i] = leftProducts[i] * rightProducts[i]

    return aop
