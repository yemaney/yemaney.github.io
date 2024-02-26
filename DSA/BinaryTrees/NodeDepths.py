"""
Given:
- Binary Tree

Return:
- sum of all the binary tree's nodes depths
"""
from __init__ import BinaryTree, Node

# Inputs
tree = BinaryTree(1).insert([2, 4, 8, 9, 5, 3, 6, 7])


# Solution #1
def nodeDepths1(root):
    """
    Create an initial depth sum of 0, and a last of dictionaries with
    the node and its depth.

    Check node for validity, append it's children to stack. If node is
    None, don't try to append children. Continue until stack is empty.
    Essentially

    time: O(n) -> have to traverse to every node
    spaceL O(h) => h is height of binary tree, storage increases to
    a max of the tree height.
    """
    depthSums = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        depthSums += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return depthSums


# Solution #2
def nodeDepths2(root, depth=0):
    """
    Start with 0 depth. Recursively, travel to its children while
    incrementing the depth. Recursively, sum up the depths of each
    child.
    Leaf node return zero to enable addition all the way back up.

    time: O(n) -> have to traverse to every node
    spaceL O(h) => h is height of binary tree, storage increases to
    a max of the tree height.
    """
    if root is None:
        return 0
    return (
        depth + nodeDepths2(root.left, depth + 1) + nodeDepths2(root.right, depth + 1)
    )
