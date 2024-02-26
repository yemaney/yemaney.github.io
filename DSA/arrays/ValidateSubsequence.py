"""
Given two non-empty arrays of integers, return a function that
determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily 
adjacent in the array but are in the same order.

Example: [1,3,4] is a subsequence of [0,1,2,3,4]
"""

# Inputs
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

# Solution #1
def isValidSubsequence1(array: list, sequence: list) -> bool:
    """
    Create pointers at begginning of array and sequence.
    
    Move array pointer if elements don't match, move sequence
    pointer if a match is found. If sequence is a valid subsequence
    the sequence pointer should be the length of the sequence.
    
    time: O(n) -> traversing entire array
    space: O(1) -> only storing pointers
    """
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


# Solution #2
def isValidSubsequence2(array: list, sequence: list) -> bool:
    """
    Create pointers for begginning  sequence.
    
    Check if sequence at pointer is in array. If it is, increment
    pointer. Break if pointer is equal to length of sequence.
    
    time: O(n) -> traversing entire array
    space: O(1) -> only storing pointers   
    """
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)
    