#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """Subclass of list"""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
