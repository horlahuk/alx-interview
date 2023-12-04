#!/usr/bin/python3
'''Lockboxes task'''
def canUnlockAll(boxes):
    """Determines if all the boxes can be opened.
    Args:
        boxes: list of lists of integers.
    Returns:
        True if all boxes can be opened, else return False.
    """
    if not boxes:
        return False
    if len(boxes) == 1:
        return True
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
