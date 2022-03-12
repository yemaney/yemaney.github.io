"""
Write a function that takes in an integer n and returns the nth
Fibonacci number.
"""

# inputs
n = 6

# Solution 1
def getNthFib(n: int) -> int:
    """
    Return 0 or 1 if n is 1 or 2. Else, recursively call the function
    to sum up the fibonacci numbers.

    time: O(2^n) -> calling the function 2^n times
    space: O(n) -> storing at most n functions in the call stack
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n - 2) + getNthFib(n - 1)


# Solution #2
def getNthFib2(n: int) -> int:
    """
    Create x, y as placeholders for first two elements in the
    fibonacci sequence. For every number n is above 1, perform the
    fibonacci operation.

    time: time(n) -> looping scales size of n
    space: O(1) -> only storing x and y
    """
    x, y = 0, 1
    while n > 1:
        n -= 1
        x, y = y, x + y
    return x
