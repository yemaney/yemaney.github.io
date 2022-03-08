"""
Given:
- Node that has a name and an array of optional children

Return:  Implement a depth first search (left-to-right)
- return all the node names in an array and return
- 
"""

# Inputs
data = {
    "nodes": [
        {"children": ["B", "C", "D"], "id": "A", "value": "A"},
        {"children": ["E", "F"], "id": "B", "value": "B"},
        {"children": [], "id": "C", "value": "C"},
        {"children": ["G", "H"], "id": "D", "value": "D"},
        {"children": [], "id": "E", "value": "E"},
        {"children": ["I", "J"], "id": "F", "value": "F"},
        {"children": ["K"], "id": "G", "value": "G"},
        {"children": [], "id": "H", "value": "H"},
        {"children": [], "id": "I", "value": "I"},
        {"children": [], "id": "J", "value": "J"},
        {"children": [], "id": "K", "value": "K"},
    ],
    "startNode": "A",
}

# solution #1
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        """
        Since the children are in arrays, looping over them will ensure
        the algorithm goes from left to right. Recursively call the
        depthFirstSearch method for each child found, and append to list.

        time: O(v+e) -> where v, e = vertices and edges traveled
        space:O(v) -> worst case when tree is one long branch
        """
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


graph = Node("A")
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")
dfs = graph.depthFirstSearch([])
print(dfs)
