"""
Write a Binary Search Tree Class. That supports:
1. Inserting values with `insert` method
2. Removing values with the `remove` method, this method should only
    remove  the first instance of a given value.
4. Can't remove if only one node is available.
3. Searching for values with the `contains` method
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        """
        All main methods using binary search to find values. Iterative approach
        to avoid growing call stack that occurs when using recursive algorithms.
        Changes are made in place, by reassigning pointers between tree nodes.
        
        time: O(log(n))
        space: O(1)
        """

    def insert(self, value):

        currentNode = self

        while currentNode is not None:

            if value >= currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                currentNode = currentNode.left

        return self

    def contains(self, value):
        currentNode = self

        while currentNode is not None:
            if currentNode.value == value:
                return True
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left

        return False

    def remove(self, value, parentNode=None):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:  # move left
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:  # move right
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    """
                    if currentNode had two children, remove replace with leftmost leaf
                    node of right subtree
                    """
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    """
                    Case of root node with one child.
                    """
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        # this is a single node tree, do nothing
                        pass

                elif (
                    parentNode.left == currentNode
                ):  # case of current node having one child
                    if currentNode.left is not None:
                        parentNode.left = currentNode.left
                    else:
                        parentNode.left = currentNode.right
                elif parentNode.right == currentNode:
                    if currentNode.left is not None:
                        parentNode.right = currentNode.left
                    else:
                        parentNode.right = currentNode.right
                break

        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
