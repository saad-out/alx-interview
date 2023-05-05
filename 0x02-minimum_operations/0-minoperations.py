#!/usr/bin/python3


def minOperations(n: int) -> int:
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
