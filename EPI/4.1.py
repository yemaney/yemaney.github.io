# Computing parity of a binary word
# 1 if number  of 1's is odd, else 0


def parity_brute(word: int) -> int:
    """
    Brute force parity algorithm.
    Loop:
        1. calculate XOR of result and lowermost bit of word
            - Which Checks if lowermost bit is a 1
            - 1^1=0, 1^0=1, 0^0=0
        2. bit shift word
    """
    result = 0
    while word:
        # checks if first bit is a 1
        result ^= word & 1

        #  bit shift word
        word >>= 1
    return result


def parity_2(word: int) -> int:
    result = 0
    while word:
        result ^= 1
        word &= word - 1  # drop lowest set bit
    return result


if __name__ == "__main__":
    pb = parity_brute(3)
    print(pb)

    p2 = parity_2(3)
    print(p2)
