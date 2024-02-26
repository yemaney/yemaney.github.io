"""
Given:
An array of integers representing the distances between cities.
An array of integers representing the amount of fuel that can be picked up at each city,
An integer representing the mpg a car gets.

Return:
The index of the valid starting city, such that one can make a full cycle without running
out of fuel if they start the trip there.
"""

from __future__ import annotations

# inputs
distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

# Solution
def validStartingCity(distances: list[int], fuel: list[int], mpg: int) -> int:
    """
    Loop through a full cycle once. The city with the smallest miles remaining
    is the starting city.


    time : O(n) -> looping through entire distances array
    space: O(1)
    """
    milesRemaining = 0

    startingCity = 0
    milesRemainingAtStart = 0

    for i in range(1, len(distances)):
        lastDistance = distances[i - 1]
        lastFuel = fuel[i - 1]
        milesRemaining += lastFuel * mpg - lastDistance

        if milesRemaining < milesRemainingAtStart:
            milesRemainingAtStart = milesRemaining
            startingCity = i
    return startingCity
