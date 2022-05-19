"""
Given:


Return:
"""
from __future__ import annotations

# inputs
matrix = [[0, -1, -3, 2, 0], [1, -2, -5, -1, -3], [3, 0, 0, -4, -1]]


def minimumPassesOfMatrix(matrix: list[list[int]]) -> int:
    """
    Get all positions in matrix that have a positive value into a queue. Iterate
    over these positions and turn any of there negative neighbors into positive.
    Then append the neighbors position to a new queue. Repeat iteration on new queue
    until a new queue is empty, then check if there is still a negative in the matrix.

    time: O(w * h)
    space : O(w * h)
    """

    nextQueue = getAllPositives(matrix)
    passes = 0

    while len(nextQueue) > 0:
        currentQue = nextQueue
        nextQueue = []

        while len(currentQue) > 0:
            i, j = currentQue.pop()

            adjacentPositions = getAdjacent(matrix, i, j)
            for position in adjacentPositions:
                i, j = position
                if matrix[i][j] < 0:
                    matrix[i][j] *= -1
                    nextQueue.append([i, j])
        passes += 1

    stillContainsNegative = containsNegative(matrix)
    return passes - 1 if not stillContainsNegative else -1


def getAllPositives(matrix: list[list[int]]) -> list[list[int]]:
    positives = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] > 0:
                positives.append([i, j])
    return positives


def getAdjacent(matrix: list[list[int]], i: int, j: int) -> list[list[int]]:
    adjacent = []

    if i > 0:
        adjacent.append([i - 1, j])
    if i < len(matrix) - 1:
        adjacent.append([i + 1, j])
    if j > 0:
        adjacent.append([i, j - 1])
    if j < len(matrix[0]) - 1:
        adjacent.append([i, j + 1])
    return adjacent


def containsNegative(matrix: list[list[int]]) -> bool:
    for row in matrix:
        for val in row:
            if val < 0:
                return True
    return False
