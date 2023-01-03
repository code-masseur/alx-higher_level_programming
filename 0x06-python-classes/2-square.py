#!/usr/bin/python3

"""This module defines a class 'Square'
"""


class Square:
    """This is a simple 'Square' class.
    Attribute:
        size (int): the size of the 'Square'.
    """
    def __init__(self, size=0):
        """Constructs a 'Square' object.
        Args:
            __size (int): the size of the 'Square'.
                the default value is 0
        Raises:
            TypeError: if '__size' is not an integer.
            ValueError: if '__size' is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
