"""
Given: two positive integers representing the width and height of a rectangular
grid.

Return:
The number of wys to reach the bottom right corner of the graph when starting from
top left corner. Each move you make must go up or right.
"""


# inputs
width = 4
height = 3

# Solution 1
def numberOfWaysToTraverseGraph1(width: int, height: int) -> int:
    """
    Make a grid of size width * height. All boxes on the first row and first
    column of the grid have 1. Every other box value is the sum of the boxes
    directly above and to the left.

    time: O(n*m) : traversing through every box in grid
    space: O(n*m) : creating a grid of n(m size)
    """

    grid = [[0 for _ in range(width)] for _ in range(height)]

    for w in range(width):
        for h in range(height):
            if w == 0 or h == 0:
                grid[h][w] = 1
            else:
                left = grid[h][w - 1]
                up = grid[h - 1][w]
                grid[h][w] = left + up

    return grid[height - 1][width - 1]


# Solution 2
def numberOfWaysToTraverseGraph2(width: int, height: int) -> int:
    """
    Now matter which path is taken. The same number of down and right steps
    will have to be taken to get from the top left to the bottom right of the
    graph. Thus the number of unique paths is the number of unique permutations
    of down and right steps possible.

    time: O(n*m) : for the permutation calculation
    space: O(1) : only keeping track of 2 numbers
    """

    rightMoves = width - 1
    downMoves = height - 1

    numerator = factorial(rightMoves + downMoves)
    denominator = factorial(rightMoves) * factorial(downMoves)

    return numerator // denominator


def factorial(num):
    result = 1

    for n in range(2, num + 1):
        result *= n
    return result
