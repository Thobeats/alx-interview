#!/usr/bin/python3
"""UTF8 Module"""

def validUTF8(data):
    """ValidUTF8

    Keyword arguments:
    data -- validates the utf8
    Return: True or False
    """

    bytes_remaining = 0

    for byte in data:
        byte = byte & 0xFF

        if bytes_remaining == 0:
            if byte >> 5 == 0b110:
                bytes_remaining = 1
            elif byte >> 4 == 0b1110:
                bytes_remaining = 2
            elif byte >> 3 == 0b11110:
                bytes_remaining = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bytes_remaining -= 1

    return bytes_remaining == 0
