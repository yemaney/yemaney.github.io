"""
Given:
A non empty sorted array of distinct integers.

Return:
Write a function that constructs a BST from the input array and
return the root of the BST. Height of BST should be minimized.
"""
from __future__ import annotations

array = [1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36]


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

        return self


def minHeightBstHelper(array: list, start: int, end: int) -> BST | None:
    """
    BST with minimum height, is a BST that is as even as possible. This is done
    by selecting the middle number in a sorted list as the root node. Splitting
    this list into two list, one for each subtree (left and right). Recursively
    choose a node for each subtree using the same criteria.

    time: O(n) -> traversing through each node
    space: O(n) -> creating a BST with n nodes
    """
    if end < start:
        return None
    mid = (start + end) // 2
    bst = BST(array[mid])
    bst.left = minHeightBstHelper(array, start, mid - 1)
    bst.right = minHeightBstHelper(array, mid + 1, end)
    return bst


def minHeightBst(array):
    return minHeightBstHelper(array, 0, len(array) - 1)
