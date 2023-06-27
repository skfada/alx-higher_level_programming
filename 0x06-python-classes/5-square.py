#!/usr/bin/python3
"""a class Square that defines a square by: (based on 4-square.py )"""

class Square:
    """A square class"""

    def __init__(self, size=0):
        """initializes square
        Args:
            size (int): size of the square
        """

        self.size = size

    @property
    def size(self):
        """the value of size
        Returns:
            size (int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Change the value of size
        Args:
            value (int): the new value of size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """the area of a square
        Returns:
            area
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the value of a square"""
        if self.__size == 0:
            print("")
        for index in range(0, self.__size):
            for count in range(0, self.__size):
                print("#", end="")
            print()
