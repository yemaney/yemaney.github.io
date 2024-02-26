"""
Given:
Two arrays of the speeds of, blue shirt bikers and red shirt bikers. Two
people of different color shirts will ride a bike together. Bike speed
is the maximum of the two peoples speed. 

A parameter named fastest.

Return:
If fastest=True, maximum possible total speed. Otherwise minimum possible
total speed. Total speed is the speed of all tandem bikes summed.
"""

# Inputs
redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = True

# Solution #1
def tandemBicycle(redShirtSpeeds: list, blueShirtSpeeds: list, fastest: bool) -> int:
    """
    Pair up slowest reds with fastest blues to get maximum total speed, or slowest reds
    with slowest blues to get minimum total speed.

    time:   O(nlog(n)) -> sorting
    space:  O(1) -> not storing
    """

    cumSpeed = 0
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)

    for x, y in zip(redShirtSpeeds, blueShirtSpeeds):
        cumSpeed += max(x, y)

    return cumSpeed
