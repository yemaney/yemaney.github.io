"""
Given:
An array of distinc positive integers representing coin denominations.
A single non-negative integer n representing a target amount of money.

Return:
The number of ways to create the target amount using the coins.
"""

# Inputs
n = 6
denoms = [1, 5]

# Solution
def numberOfWaysToMakeChange(n: int, denoms: list) -> int:
    """
    Using each denom, figure out num of ways to build i, where i is in 0 to n.
    Continually build up using previous ways.


    time: O(nd) -> looping twice
    space: O(n) -> array of sways scales with n
    """
    
    
    numOfWays = [0 for amount in range(n+1)]
    numOfWays[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                numOfWays[amount] += numOfWays[amount-denom]

    return numOfWays[n]