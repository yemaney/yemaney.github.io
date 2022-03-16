"""
Given:
A non-empty string.

Return: 
The strings length encoding.In which runs of data are stored as a
single data value and count. A run is is a sequence of consecutive,
identical letters, special characters or numbers. 
"""

# Inputs
string = "AAAAAAAAAAAAABBCCCCDD"

# Solution #1
def runLengthEncoding(string: str) -> str:
    """
    Create a variable to keep track of current index. Iteratively check
    if the character at the concurrent index is the same character as
    the one at the current index. Early break if count is 9.

    time: O(n) -> iterating over entire string
    space: O(n) -> rle size linearly scale with string passed
    """

    rle = []
    idx = 0

    while idx < len(string):
        count = 1
        while count + idx < len(string) and string[idx + count] == string[idx]:
            if count == 9:
                break
            count += 1

        rle.append(f"{count}{string[idx]}")
        idx += count

    return "".join(rle)
