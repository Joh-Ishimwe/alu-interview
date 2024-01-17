#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to result in exactly n H characters
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters

    Args:
        n (int): The target number of H characters

    Returns:
        int: The minimum number of operations needed, or 0 if impossible
    """
    if n <= 1:
        return 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n

if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

