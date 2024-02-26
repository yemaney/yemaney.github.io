"""
Given:
Two strings.

Return:
Minimum number of edit operations that need to be performed on the first string to
obtain the second string.

There are three edit operations that can be performed:
- insert a character, delete a character, substition of a character for another one
"""

# Inputs
str1 = "abc"
str2 = "yabd"

# Solution
def levenshteinDistance(str1: str, str2: str) -> int:
    """
    Create a grid with each string acting a rows and cols. For each cell the
    the number of operations is the minimum of the cells above, to the left,
    and diagonal left of it.


    time: O(nm)
    space: O(nm)
    """
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i - 1][0] + 1
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(
                    edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1]
                )
    return edits[-1][-1]


levenshteinDistance(str1, str2)
