#!/usr/bin/python3
"""
This module contains a function that determines if a given data set represents
a valid UTF-8 encoding.
"""
BYTE = 8


def one_byte(n):
    """
    Converts a number to a binary string representation of
    least significant byte.

    Args:
        n (int): The number to convert.

    Returns:
        str: The binary string representation of the least significant byte.
    """
    bin_n = bin(n).split('b')[1]
    if len(bin_n) >= BYTE:
        return bin_n[-8:]
    else:
        return bin_n.zfill(BYTE)


def bytes_count(byte):
    """
    Determines the number of remaining bytes in a UTF-8 character.

    Args:
        byte (str): The binary string representation of the least significant

    Returns:
        int: The number of remaining bytes in a UTF-8 character.
    """
    if not byte or type(byte) != str:
        return 0

    if byte.startswith('0'):
        return 0
    elif byte.startswith('110'):
        return 1
    elif byte.startswith('1110'):
        return 2
    elif byte.startswith('1111'):
        return 3


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): The data set to validate.

    Returns:
        bool: True if the data set represents a valid UTF-8 encoding, False
    """
    continuation_byte = False
    remaining_bytes = 0
    for n in data:
        byte_n = one_byte(n)
        if not continuation_byte:
            if byte_n.startswith('10'):
                return False
            remaining_bytes = bytes_count(byte_n)
        else:
            if not byte_n.startswith('10'):
                return False
            remaining_bytes -= 1
        if remaining_bytes == 0:
            continuation_byte = False
        elif remaining_bytes > 0:
            continuation_byte = True

    if remaining_bytes > 0:
        return False
    return True
