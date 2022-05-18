"""
Given:
A list of edges representing an unweighted, directed graph with at lease one node.
For index i in the list, there is a list of integers, representing the vertices i
can travel to.

Return:
A boolean representing whether the graph contains a cycle.

A cycle is any number of vertices, including just one vertex, that are connected in a closed chain.
"""
from __future__ import annotations

# Inputs
edges = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]


# Solution
def cycleInGraph(edges: list[list[int]]) -> bool:
    """
    Create 2 boolean masks to keep track of nodes visited and the current
    stack being traversed. Each edge in edges is a stack. Recursively do a
    depth first search for each node, if you ever reach a node twice in one
    stack return true.

    time: O(v + e)
    space: O(v)
    """

    visited = [False for edge in edges]
    stack = [False for edge in edges]

    for i in range(len(stack)):
        if visited[i]:
            continue
        containsCycle = isCycle(i, edges, visited, stack)
        if containsCycle:
            return True
    return False


def isCycle(
    i: int, edges: list[list[int]], visited: list[bool], stack: list[bool]
) -> bool:
    visited[i] = True
    stack[i] = True

    neighbors = edges[i]
    for neighbor in neighbors:
        if not visited[neighbor]:
            containsCycle = isCycle(neighbor, edges, visited, stack)
            if containsCycle:
                return True

        elif stack[neighbor]:
            return True

    stack[i]

    return False
