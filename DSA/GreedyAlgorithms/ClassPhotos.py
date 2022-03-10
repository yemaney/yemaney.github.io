"""
Given:
Two arrays of heights for students. One for students with red shirts
and another for students with blue shirts.

Rule: 
Want to order student for a picture such that students of same shirt
color sit in the same row. All students in back row must be taller 
than those in front row.

Return:
Whether the students can be arranged according to the rule.
"""

# Inputs
redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]

# Solution #!
def classPhotos(redShirtHeights: list, blueShirtHeights: list) -> bool:
    """
    Sort each list in place, compare there tallest student to see which group
    would be seated in the back if the rule would be observed.
    Iterate over both lists and check if the height rule is broken to exit early
    and return False. Else return True.

    time: O(nlog(n)) -> sorting lists
    space: O(1) -> not storing anything
    """

    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    if redShirtHeights[0] > blueShirtHeights[0]:
        taller = redShirtHeights
        shorter = blueShirtHeights
    else:
        taller = blueShirtHeights
        shorter = redShirtHeights

    for x, y in zip(taller, shorter):
        if y >= x:
            return False
    return True
