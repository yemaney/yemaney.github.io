"""
Given:
- A non-empty array of positive integers
Return:
- The total minimum waiting time for all queries. A queries waiting time
is the amount it has to wait for every other query in front of it before
it executes.

Example:
[3, 2, 1, 2, 6] -> 17
"""

# Inputs
queries = [3, 2, 1, 2, 6]

# Solution #1
def minimumWaitingTime(queries):
    """
    Sort the array so the rolling cumulative waiting time is
    always comprised of the smallest numbers in the array.
    Loop through the array and sum up the cumulative waiting times.

    time: O(nlog(n)) -> due to sorting, where n is length of arrary
    space: O(0) =-> only storing some integers
    """
    queries.sort()
    waiting, cumWait = 0, 0
    for i in range(len(queries) - 1):
        waiting += queries[i]
        cumWait += waiting

    return cumWait
