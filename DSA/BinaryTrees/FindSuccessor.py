"""
Given:
A binary tree, where each node has an additional pointer to its parent.
A node contained in that tree.

Return:
Return the next node to be visited after the input node, when traversing
the tree in-order.
"""
from __future__ import annotations


# Inputs
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# Solution #1
def inOrderList(node: BinaryTree | None, array: list):
    if node is None:
        return
    inOrderList(node.left, array)
    array.append(node)
    inOrderList(node.right, array)

    return array


def findSuccessor1(tree: BinaryTree, node: BinaryTree):
    """
    Create an array of the nodes in order. Then return the i+1 element of the
    array, where i is the index of the element in the array holding node.

    time: O(n): traversing through entire tree
    space: O(n): storing a list of all nodes in the tree
    """

    array = []
    inOrderList(tree, array)

    for idx, currentNode in enumerate(array):
        if currentNode != node:
            continue

        if idx == len(array) - 1:
            return None

        return array[idx + 1]


# Solution #2
def findSuccessor2(tree: BinaryTree, node: BinaryTree):
    """
    Take advantage of the fact that input node, exists in the tree and contatins
    pointers to the child nodes and parent node. If the node has a right subtree,
    return the leftmost element of that subtree.Else, return the rightmost parent
    of the node.

    time: O(h) only going up or down a tree in one direction
    space: O(1) only holding reference to the current node, doesn't scale
    """
    if node.right is not None:
        return getLeftMostChild(node.right)
    return getRightMostParent(node)


def getLeftMostChild(node: BinaryTree):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode


def getRightMostParent(node: BinaryTree):
    currentNode = node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent

    return currentNode.parent
