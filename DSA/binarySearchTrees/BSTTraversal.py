"""
Write three functions that take a BST and an empty array. Traverse,
the BST. add its nodes to the input array, return the array.

1. inOrderTraverse: bottom left to bottom right
2. preOrderTravers: top to bottom left then to bottom left
3. postOrderTraverse: bottom left and bottom right to top
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inOrderTraverse(tree: BST, array):
    """
    time O(n): traversing to every node
    space O(n): creating an array containing all node values
    """
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree: BST, array):
    """
    time O(n): traversing to every node
    space O(n): creating an array containing all node values
    """
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree: BST, array):
    """
    time O(n): traversing to every node
    space O(n): creating an array containing all node values
    """
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array
