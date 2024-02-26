"""
Given:
An integer k, representing the number of workers.
An array of positive integers representing duration of tasks.

Return:
Th optimal assignment of tasks such that the least amount of time is spent.
Workers will work in parallel, so the pair of tasks with the longest time will be how
long it takes for everyone to complete both of their tasks.
Each worker must work must complete two unique tasks.
"""

from __future__ import annotations

# Inputs
k = 3
tasks = [1, 3, 5, 3, 1, 4]


# Solution
def taskAssignment(k: int, tasks: list) -> list[list[int]]:
    """
    Keep track of all the possible indexes for value sin tasks using a dictionary.
    Sort the tasks list, then find the optimal values, the available max and min pair.
    Find a possible index for those pair values, from the dictionary and append to
    assignment list.

    time: O(nlog(n)) : -> sorting
    space : O(n) -> creating the dict
    """
    obj = getIndexes(tasks)
    tasks.sort()

    left = 0
    right = len(tasks) - 1
    assignment = []

    while left < right:
        min, max = tasks[left], tasks[right]
        min, max = obj[min].pop(), obj[max].pop()

        assignment.append([min, max])
        left += 1
        right -= 1

    return assignment


def getIndexes(tasks: list) -> dict[int, list[int]]:
    indexObj = {}

    for idx, task in enumerate(tasks):
        if task in indexObj:
            indexObj[task].append(idx)
        else:
            indexObj[task] = [idx]

    return indexObj
