"""
Given:
A Node class that has a name and an array of optional children nodes.

Return:
Implement a breadthFirstSearchMethod on the Node class.
"""
from __future__ import annotations


# Solution
class Node:
    def __init__(self, name: str):
        self.children : list[Node] = []
        self.name = name
        
    def addChild(self, name: str):
        self.children.append(Node(name))
        return self
    
    def breadthFirstSearch(self):
        array = []
        
        queue : list[Node] = [self]
        while len(queue) > 0:
            value = queue.pop(0)
            array.append(value.name)
            
            for child in value.children:
                queue.append(child)
        return array
            