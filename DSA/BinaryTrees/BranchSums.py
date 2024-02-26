"""
Given: 
- Binary Tree

Return: 
- list of branch sums ordered from leftmost branch to rightmost branch
a branch is a path of nodes starting at the root and ending at a leaf
"""

# Inputs
tree = {
    "nodes": [
        {"id": "1", "left": "2", "right": "3", "value": 1},
        {"id": "2", "left": "4", "right": "5", "value": 2},
        {"id": "3", "left": "6", "right": "7", "value": 3},
        {"id": "4", "left": "8", "right": "9", "value": 4},
        {"id": "5", "left": "10", "right": None, "value": 5},
        {"id": "6", "left": None, "right": None, "value": 6},
        {"id": "7", "left": None, "right": None, "value": 7},
        {"id": "8", "left": None, "right": None, "value": 8},
        {"id": "9", "left": None, "right": None, "value": 9},
        {"id": "10", "left": None, "right": None, "value": 10},
    ],
    "root": "1",
}


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(Node):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])


# Solution #1
def branchSums(root: BinaryTree) -> list:
    """
    Create an empty list to carry future branch sums.
    Recursively go down the branch, (depth first), and update the
    current sum, append to the sums list when a leaf node is reached.

    time: O(n) -> have to ravel to each node
    space: O(n) - > if tree is one branch, have
    """

    sums = []
    branchSumsHelper(root, 0, sums)
    return sums


def branchSumsHelper(node: Node, currentSum: int, sums: list):
    if node is None:
        return

    currentSum += node.value
    if node.left is None and node.right is None:
        sums.append(currentSum)

    branchSumsHelper(node.left, currentSum, sums)
    branchSumsHelper(node.right, currentSum, sums)
