"""
Given:
A binary search tree, and an integer k.

Return:
The kth largest integer in the BST
"""


class BST:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reverseInOrder(node: BST, obj: dict, k: int):
    if node is None or obj["visited"] == k:
        return
    reverseInOrder(node.right, obj, k)
    if obj["visited"] < k:
        obj["visited"] += 1
        obj["latest"] = node.value

        reverseInOrder(node.left, obj, k)


def findKthLargestValueInBst(node: BST, k: int):
    """
    Create an object to keep track of how many nodes are visited and the
    current node value. Travel to to leftmost-lowermost node and work upwards
    in reverse order. Early exit when k nodes have been passed.

    time: O(h + k): go down the height (h) of tree and then traveling to k nodes
    space: O(h): Will have at max h function calls at once
    """

    obj = {"visited": 0, "latest": None}

    reverseInOrder(node, obj, k)
    return obj["latest"]
