"""
Given:
A binary tree.

Return:
Return a boolean value representing whether the input tree is height
balanced. A height balanced tree is a tree, where for ever node, the
difference in height between the nodes left and right children is at
most than 1.
"""
# Inputs
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Solution 1
def heighBalanceDFS(node: BinaryTree) -> dict:
    if node is None:
        return {"height": 0, "balanced": True}

    leftChildBalance = heighBalanceDFS(node.left)
    rightChildBalance = heighBalanceDFS(node.right)
    height = max(leftChildBalance["height"], rightChildBalance["height"]) + 1

    isBalanced = (
        leftChildBalance["balanced"]
        and rightChildBalance["balanced"]
        and abs(leftChildBalance["height"] - rightChildBalance["height"]) <= 1
    )
    return {"height": height, "balanced": isBalanced}


def heightBalancedBinaryTree(tree: BinaryTree) -> bool:
    """
    Recursively traverse through the tree using depth first search.
    Calculate the height of the left and right children, and check if
    it is balanced.

    time: O(n) -> traverseing through every node in the tree
    space: O(h) -> call stack max size of height of tree
    """
    return heighBalanceDFS(tree)["balanced"]
