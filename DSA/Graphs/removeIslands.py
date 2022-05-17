"""
Given:
A two dimensional matrix of 0's and 1's.

Return:
A modified version of the input matrix without any islands. And island is any
number of 1's that are connected horizontally or vertically. But do not touch
the border.
"""
from __future__ import annotations


def removeIslands(matrix: list[list[int]]) -> list[list[int]]:
    """
    Create a mask of same size as input matrix to keep track of positions that are
    1 and connected to a 1 in the border. Loop through each 1 in the border, and
    keep track of its neighbors that are also 1. Loop again to reset every value in
    the matrix to 0, if it is not on the border and not a 1 value connected to the
    border.

    time : O(wh) -> at max looping thorugh every element of matrix
    space : O(wh) -> creating a mask of size of the input matrix
    """

    onesConnectedToBorder = [[False for value in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            rowIsBorder = i == 0 or i == len(matrix) - 1
            colIsBorder = j == 0 or j == len(matrix[0]) - 1

            # skip if current position is not on border
            if not (rowIsBorder or colIsBorder):
                continue
            # skip if border value is not a 1
            if matrix[i][j] != 1:
                continue
            # find other 1's connected to the border
            findOnesConnectedToBorder(matrix, i, j, onesConnectedToBorder)

    # for every element that is not conencted to a 1 in thethe border, make its value 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0])):
            if onesConnectedToBorder[i][j]:
                continue
            matrix[i][j] = 0

    return matrix


def findOnesConnectedToBorder(
    matrix: list[list[int]], i: int, j: int, onesConnectedToBorder: list[list[bool]]
):
    # start with the first coordinate that is a 1 value in the border
    stack = [[i, j]]

    while len(stack):
        currentPosition = stack.pop()
        i, j = currentPosition

        # check if it is already visited to avoid work duplication
        alreadyVisited = onesConnectedToBorder[i][j]
        if alreadyVisited:
            continue

        onesConnectedToBorder[i][j] = True

        # get neighbors of current position
        neighbors = getNeighbors(matrix, i, j)
        for neighbor in neighbors:
            row, col = neighbor

            if matrix[row][col] != 1:
                continue
            stack.append(neighbor)


def getNeighbors(matrix: list[list[int]], i: int, j: int) -> list[list[int]]:
    neighbors = []

    # checking up down left right
    if i - 1 >= 0:
        neighbors.append([i - 1, j])
    if i + 1 < len(matrix):
        neighbors.append([i + 1, j])
    if j - 1 >= 0:
        neighbors.append([i, j - 1])
    if j + 1 < len(matrix[0]):
        neighbors.append([i, j + 1])

    return neighbors
