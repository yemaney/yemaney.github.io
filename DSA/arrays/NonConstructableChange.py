"""
Give: 
- an array of positive integers representing coin values

Return:
- The minimum sum of money that cannot be created with coins available

Example:
- coins = [1,2,5] -> 4
"""

# Inputs
coins = [5, 7, 1, 1, 2, 3, 22]

# Solution #1
def nonConstructibleChange(coins):
    """
    Sort the coins, and create a variable storing maximum change
    that can be created at 0.

    Iterate over the coins. If the current coin is = to currentChange + 1,
    then the next successive change can be created. If the current coin >
    than currentChange + 1, then the next change can not be created.

    This works because:
    If (1 - n) change can be made. And the next coin is n + 2.
    Then n+1 doesn't exist as a coin or can't be created using all other coins.
    """
    coins.sort()
    currentChange = 0
    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1
        currentChange += coin

    return currentChange + 1
