"""
Given:
Singly linked list whose nodes are sorted in order. Each node
has a integer value as well as a next node pointing to either
the next node in the list or None if it is the tail.

Return:
A modified version of the linked list that doesn't contain any
nodes.
"""

# Inputs
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


LL = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])

# Solution #1
def removeDuplicatesFromLinkedList(linkedList: LinkedList):
    """
    Start at head node, and look forward to next node. As long as the
    next node is the same as the current, keep looking forward. When
    reaching the last node matching, update the current node to point to
    it.

    time: O(n): -> have to traverse all nodes in liked list
    space: O(1) -> storing nothing, changing the linked list in place
    """
    current = linkedList

    while current:
        nextNode = current.next
        while nextNode and nextNode.value == current.value:
            nextNode = nextNode.next

        current.next = nextNode
        current = nextNode
    return linkedList
