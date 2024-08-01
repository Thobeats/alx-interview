#!/usr/bin/python3
""" LockBoxes
This Module defines a function that finds the keys
to all the boxes
"""


def canUnlockAll(boxes):
    """canUnlockAll

    Keyword arguments:
    boxes -- a list of lists of all the boxes
    Return: true if all boxes can be unlocked else false
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
