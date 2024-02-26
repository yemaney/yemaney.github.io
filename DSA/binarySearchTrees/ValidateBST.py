"""
Given:
A potentially valid Binary Search Tree.

Return:
Return a boolean representing whether the BST is valid.
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree: BST, maxValue=float("inf"), minValue=float("-inf")):
    """
    Travel down BST using DFS. Return False if BST property is ever broken. Return True
    when a leaf node is reached. If all validation pass, then final return is True.

    time: O(n) -> traversing entire tree
    space: O(d) -> where d is tree depth, will have at max d sized call stack
    """

    if tree is None:
        return True

    if tree.value >= maxValue or tree.value < minValue:
        return False

    rightIsValid = validateBst(tree.right, maxValue=maxValue, minValue=tree.value)
    LeftIsValid = validateBst(tree.left, maxValue=tree.value, minValue=minValue)

    return LeftIsValid and rightIsValid
