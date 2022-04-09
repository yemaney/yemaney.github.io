"""
Given:
A binary tree.

Return:
The tree's diameter. A binary trees diameter is the length of the longest path
of nodes in the tree.
"""
# Inputs
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Solution
def binaryTreeDiameter(tree):
    """
    Traverse through tree using depth first search. Recursively return a dictionary
    that keeps track of the height of the current node and the maximum diameter.
    
    
    time: O(n) -> traversing through every node of the tree
    space: O(d) -> where d is depth of tree, will have max d functions on call stack
    """
    return travel(tree)

def travel(node):
	if node is None:
		return {"diameter": 0, "height": 0}
	
	l = travel(node.left)
	r = travel(node.right)
	
	heightSum = l["height"] + r["height"]
	maxDiam = max(l["diameter"], r["diameter"])
	currentHeight =  max(l["height"], r["height"]) + 1
	currentDiam = max(heightSum, maxDiam)
	
	return {"diameter": currentDiam, "height": currentHeight}
