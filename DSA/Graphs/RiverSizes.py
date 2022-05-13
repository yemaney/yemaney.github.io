"""
Given:
A two dimensional array containing 0's and 1's. Each 0 represents land, and each 1
represents part of a river. A river is any number of 1's connected either vertically
or horizontally.

Return:
An array of the sizes of all the riveres in the input matrix.
"""

from __future__ import annotations

# Inputs
matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

# Solution
def riverSizes(matrix: list[list[int]]) -> list[int]:
    """
    Create a matrix the same size as the input matrix to keep track of all the nodes
    that are visited. Do a depth first search to find the length of rivers. Skip any
    nodes that have already been visited.

    time: O(w*h) -> visiting every node
    space: O(w*h) -> creating a matrix of same size as the input matrix
    """

    sizes = []
    visited = [[False for value in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes


def traverseNode(
    i: int,
    j: int,
    matrix: list[list[int]],
    visited: list[list[bool]],
    sizes: list[int],
) -> None:
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1

        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)

    if currentRiverSize:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbors(
    i: int, j: int, matrix: list[list[int]], visited: list[list[bool]]
) -> list[list[int]]:
    unvisitedNeighbors = []
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])

    return unvisitedNeighbors
