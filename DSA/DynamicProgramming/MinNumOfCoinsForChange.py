"""
Given:
An array of positive integers representing coin denominations.
A single non-negative integer n representing a target amount of money.

Return:
The minimum number of coins required to create the target amount.
"""

from __future__ import annotations

# Inputs
n = 7
denoms = [1, 5, 10]

# Solution
def minNumOfCoinsForChange(n: int, denoms: list[int]):
    """
    Find minimum number of coins needed to create change for each amount using
    the first denom. Then see how adding one more denom each time affects it.

    time: O(nd)
    space: O(n)
    """

    numOfCoins = [float("inf") for amount in range(n + 1)]
    numOfCoins[0] = 0

    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(
                    numOfCoins[amount], numOfCoins[amount - denom] + 1
                )
    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1
