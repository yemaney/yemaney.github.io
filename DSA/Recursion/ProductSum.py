"""
Given:
Special array, that holds integers and nested special arrays of integers.

Return:
The product sum of each special array. Product sum is the sum of each
element in the array, multiplied by the array's depth.

Example:
[5, 2, [7, -1], 3, [6, [-13, 8], 4]]

5 + 2 + 2*[7-1] + 3 + 2*[6 + 3*[-13 + 8] + 4] = 12
"""

# Inputs
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

# Slution #1
def productSum(array: list, depth: int = 1) -> int:
    """
    Loop through each element of the array. If the element is an int,
    add it to total. Elif, the element is a list of integers, recursively
    call the function on it to calculate the sum. For each case multiply
    the total returned by the depth, which is incremented for each
    recursive call.

    time: O(n) -> have to traverse thorugh n elements of the array
    space: O(d) -> where d is maximum depth, which implies the largest call
    stack that will be stored
    """

    total = 0
    for element in array:
        if isinstance(element, int):
            total += element
        elif isinstance(element, list):
            total += productSum(element, depth + 1)
    return depth * total
