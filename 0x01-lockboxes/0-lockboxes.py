#!/usr/bin/python3
"""
This module contains a function to solve the lockboxes algorrithm problem
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
        boxes (list): list of boxes

    Return:
        (bool) True if all boxes can be opened, false otherwise
    """
    if not boxes or len(boxes) == 1:
        return True

    return unlockBox(0, {}, boxes)


def unlockBox(current_box, boxes_keys, boxes):
    """
    Unlocks a box and checks if all boxes are unlocked

    Args:
        current_box (int): current box to unlock
        boxes_keys (dict): dictionary of boxes and their status
        boxes (list): list of boxes

    Return:
        (bool) True if all boxes are unlocked, false otherwise
    """
    if current_box < 0 or current_box >= len(boxes):
        raise IndexError("current_box out of range")

    boxes_keys[current_box] = True
    for key in boxes[current_box]:
        if key not in boxes_keys.keys():
            boxes_keys[key] = False

    if len(boxes_keys) == len(boxes):
        return True

    for key, unlocked in boxes_keys.items():
        if (not unlocked) and (key < len(boxes) and key >= 0):
            return unlockBox(key, boxes_keys, boxes)
    return False
