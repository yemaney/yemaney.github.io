"""
Given:
- A binary search tree
    - each Node has ab Integer value, a left child node and a right child
    node   

- target integer value

Return:
- closest value in the binary search tree to the given target
"""

# Inputs
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = Node(10)
        self.root.left = Node(5)
        self.root.left.left = Node(2)
        self.root.left.left.left = Node(1)
        self.root.left.right = Node(5)
        self.root.right = Node(15)
        self.root.right.left = Node(13)
        self.root.right.left.right = Node(14)
        self.root.right.right = Node(22)


target = 12
tree = BST()

# Solution #1
def findClosestValueInNode1(tree: Node, target: int) -> int:
    """
    Start at root node.

    Call a function to check current node is closer
    to target value than current closest.

    If it is, update closest value. Continue to call the function
    recursively, moving down the BST until you reach a left node.

    Average:
    time: O(log(n)) - > where n is the number of nodes
    space: O(log(n))
    Worst case (one long branch):
    time: O(n)
    space: O(n)
    """
    return findClosestHelper(tree.root, target, tree.root.value)


def findClosestHelper(node: Node, target: int, closest: int) -> int:
    if node is None:
        return closest

    if abs(target - closest) > abs(target - node.value):
        closest = node.value
    if target < node.value:
        return findClosestHelper(node.left, target, closest)
    elif target > node.value:
        return findClosestHelper(node.right, target, closest)
    else:
        return closest


# Solution #2
def findClosestValueInNode2(node: Node, target: int):
    """
    Start at root node. 
    
    Check if the current node is closer to the target than current 
    closest. If so update the current closes.
    
    Move down the tree, so long as the current node is not None.
    
    
    Average:
    time: O(log(n)) - > where n is the number of nodes
    space: O(1) -> not storing recursive function stacks in memory
    Worst case (one long branch):
    time: O(n)
    space: O(1)
    """
    
    currentClosest = node.value

    while node is not None:
        if abs(target - closest) > abs(target - node.value):
            currentClosest = node.value
        if target < node.value:
            node = node.left
        elif target > node.value:
            node = node.right

    return currentClosest
