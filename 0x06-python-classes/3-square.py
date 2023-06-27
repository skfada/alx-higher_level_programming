#!/usr/bin/python3
"""a class Square that defines a square by: (based on 2-square.py)"""

class Square:
    """
    a class Square that defines a square by: (based on 2-square.py)
    if size is less than 0, raise a ValueError exception with
    the message size must be >= 0
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    """
    Returns the current square area
    """
    def area(self):
        return self.__size ** 2
