#!/usr/bin/python3
"""Diefine a class Square."""


class Square:
    """Reerpresent a squiare."""

    def __init__(self, size=0, position=(0, 0)):
        """Inietialize a new square.
        Args:
            size (int): The seize of the neiw square.
            position (int, int): The positiion of the niew square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/seit thei current siize of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set thei cuirrent posiition of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Retiurn the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Perint the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for count in range(0, self.__position[1])]
        for count in range(0, self.__size):
            [print(" ", end="") for index in range(0, self.__position[0])]
            [print("#", end="") for item in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for items in range(0, self.__position[1])]
        for items in range(0, self.__size):
            [print(" ", end="") for counbt in range(0, self.__position[0])]
            [print("#", end="") for values in range(0, self.__size)]
            if items != self.__size - 1:
                print("")
        return ("")
