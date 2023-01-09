#!/usr/bin/python3

"""This module defines a simple class 'Sqaure'
"""


class Square:
    """A simple class ''Square''.
        Attributes:
            size (int): the size of the sqaure attribute
                initial value is 0
    """

    def __init__(self, size=0):
        """Instantiating an object of the 'Square' class.
            Args:
                size (int): the size of the square
                    default value is 0
            Raises:
                TypeError: if size is not an integer
                ValueError: if size is < 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Computes the area of the square.
            Return:
                int: the area of the sqaure
        """
        return(self.__size ** 2)
