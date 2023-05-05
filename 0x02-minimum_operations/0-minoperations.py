#!/usr/bin/python3
"""
This module contains a function that calculates the minimum number of
operations required to
obtain a string of length n containing only the character 'A', using
the following two operations:

1. Add the character 'A' to the end of the string.
2. Copy the entire string and paste it to the end of the current string.
"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations required to obtain a
    string of length n
    containing only the character 'A', using the following two operations:

    1. Add the character 'A' to the end of the string.
    2. Copy the entire string and paste it to the end of the current string.

    Args:
    n (int): The length of the target string.

    Returns:
    int: The minimum number of operations required to obtain the
        target string.
    """
    if n <= 1:
        return 0

    operations: int = 2
    current_characters: int = 2
    add_by: int = 1

    while n != current_characters:
        if n % current_characters == 0:
            add_by = current_characters
            current_characters *= 2
            operations += 2
        else:
            current_characters += add_by
            operations += 1

        if current_characters > n:
            return 0

    return operations
