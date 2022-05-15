"""
Given:
Three tree inputs, where each input has an ancestor propert representing its parent tree.

Return:
The youngest common ancestor amount the first and second input descendant trees.
"""

from __future__ import annotations


# inputs
class AncestralTree:
    def __init__(self, name: str):
        self.name = name
        self.ancestor: AncestralTree | None = None


# solution
def getYoungestCommonAncestor(
    descendantOne: AncestralTree, descendantTwo: AncestralTree
) -> AncestralTree:
    """
    First make sure both descenant trees are on the same level, by equalizing their depths.
    Then move both trees up until they intersect.

    time: O(d) time
    space: O(1)
    """
    depthOne, depthTwo = get_depth(descendantOne), get_depth(descendantTwo)

    if depthOne > depthTwo:
        descendantOne = equalize_depth(descendantOne, depthOne - depthTwo)
    else:
        descendantTwo = equalize_depth(descendantTwo, depthTwo - depthOne)

    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return descendantOne


def get_depth(tree: AncestralTree) -> int:
    i = 0
    while tree is not None:
        tree = tree.ancestor
        i += 1
    return i


def equalize_depth(tree: AncestralTree, i: int) -> AncestralTree:
    for _ in range(i):
        tree = tree.ancestor
    return tree
