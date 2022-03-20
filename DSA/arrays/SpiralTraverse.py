"""
Given:
A two dimensional array.

Return:
A one dimensional array of all the input arrays elements in spiral
oder.
"""
from typing import List

# Inputs
array = [[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]]


# Solution #1
def spiralTraverse(array: List[List[int]]) -> List[int]:
    """
    Create pointers for the first element of the two dimensiona array.
    Walk along the array according to the turn strategy, and append
    elements on the way. Decrement the available vertical or horizontal
    room to walk on whenever the a turn moving in the perpendicular direction
    is complete.

    time: O(n) -> traverse over entire array
    space: O(n) -> creating a new array of same number of elements
    """

    spiral = []

    turn = "right"
    h = 0
    v = 0

    x, y = 0, 0
    while True:
        if len(array[0]) - h == 0 or len(array) - v == 0:
            break

        elif turn == "right":
            steps = 0
            for i in range(len(array[0]) - h):
                spiral.append(array[x][y + i])
                steps += 1

            v += 1
            y += steps - 1
            turn = "down"
            x += 1
        elif turn == "down":
            steps = 0
            for i in range(len(array) - v):
                spiral.append(array[x + i][y])
                steps += 1

            h += 1
            x += steps - 1
            turn = "left"
            y -= 1
        elif turn == "left":
            steps = 0
            for i in range(len(array[0]) - h):
                spiral.append(array[x][y - i])
                steps += 1

            v += 1
            y -= steps - 1
            turn = "up"
            x -= 1
        else:  # turn == "up":
            steps = 0
            for i in range(len(array) - v):
                spiral.append(array[x - i][y])
                steps += 1
            h += 1
            x -= steps - 1
            turn = "right"
            y += 1

    return spiral


# Solution #2
def spiralTraverse(array: List[List[int]]) -> List[int]:
    """
    Create pointers to four edges of the two-dimensional matrix.
    Walk along the perimeter of the matrix, then reassign the pointers to
    inner square.

    time: O(n) -> traverse over entire array
    space: O(n) -> creating a new array of same number of elements
    """

    spiral = []

    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:

        # right
        for col in range(startCol, endCol + 1):
            spiral.append(array[startRow][col])
        # down
        for row in range(startRow + 1, endRow + 1):
            spiral.append(array[row][endCol])
        # left
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:  # single row check
                break
            spiral.append(array[endRow][col])
            print(endRow, col)
        # up
        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:  # single column check
                break
            spiral.append(array[row][startCol])
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return spiral
