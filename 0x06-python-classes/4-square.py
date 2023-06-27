#!/usr/bin/python3
"""a class Square that defines a square by: (based on 3-square.py)"""

class Square:
    """a class Square that defines a square by: (based on 3-square.py)"""

    def __init__(self, size=0):
        """initializes square
        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """Gets value of size
        Returns:
            size (int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Change the value of size
        Args:
            value is an integer
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area of a square
        Returns the area
        """
        return self.__size * self.__size
