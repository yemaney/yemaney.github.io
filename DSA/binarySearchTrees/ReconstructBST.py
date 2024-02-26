"""
Given:
An array representing the pre-order traversal of a binary search tree.

Return:
Create the correct BST and return the root node.
"""
# Inputs
preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Solution #1
def reconstructBst1(preOrderTraversalValues):
    """
    Use depth first search for each element in input array to figure out where
    in the tree it belong.

    time: O(nlog(n)) -> binary search log(n) for each element in array
    space: O(n) -> creating a tree of n nodes
    """
    root = None
    for i in preOrderTraversalValues:
        if root is None:
            root = BST(i)
            continue
        dfs(root, i)

    return root


def dfs(node, value):
    # print(value)
    if node.value > value:
        if node.left:
            dfs(node.left, value)
        else:
            node.left = BST(value)
    else:
        if node.right:
            dfs(node.right, value)
        else:
            node.right = BST(value)


# Solution #2
def reconstructBst(preOrderTraversalValues):
    obj = {"idx": 0}
    return reconstructHelper(float("-inf"), float("inf"), preOrderTraversalValues, obj)


def reconstructHelper(lower, upper, array, obj):
    """
    Recursively fill build the left and right subtrees, using values grabbed by
    indexing the input array. Increment the index each time a valid tree is found.

    time: O(n) -> iterating over the input array only once
    space: O(n) -> creating a tree of n nodes
    """

    if obj["idx"] == len(array):
        return

    rootValue = array[obj["idx"]]
    if rootValue < lower or rootValue >= upper:
        return

    obj["idx"] += 1
    leftSubtree = reconstructHelper(lower, rootValue, array, obj)
    rightSubtree = reconstructHelper(rootValue, upper, array, obj)
    return BST(rootValue, leftSubtree, rightSubtree)
