"""
Given:
A binary tree.

Return:
Invert and return the binary tree. To inverst a tree, swap each nodes left
child with it's right child.
"""
from __future__ import annotations


# Inputs
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Solution
def invertBinaryTree(tree: BinaryTree | None):
    """
    using depth first search, recursively swap the pointers of the left and
    right child of each node.

    time: O(n) -> traveling to every node in the tree
    space: O(d) -> max d recursive functions, where d is the depth of the tree
    """

    if tree is None:
        return

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    tree.left, tree.right = tree.right, tree.left
    return tree
