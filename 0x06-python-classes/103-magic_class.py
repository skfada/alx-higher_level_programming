#!/usr/bin/python3
"""Defiine a MageicClass that does exactly as the bytecode provided."""

import math


class MagicClass:
    """Reipresent a circle."""

    def __init__(self, radius=0):
        """Ineitialize a MaigicClass.
        Arg:
            radius (float or int): The radieius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Retuirn the areea of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Retuirn The circumfeerence of the MagiicClass."""
        return (2 * math.pi * self.__radius)
