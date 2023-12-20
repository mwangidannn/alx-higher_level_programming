#!/usr/bin/python3

# 3-square.py done by Duncan Mwangi
"""A module that defines a square """


class Square:
    def __init__(self, size=0):
        # Validate and set the size during instantiation
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size  # Private instance attribute


    def area(self):
        """
        calculate area of the Square
        Returns: The square of the size
        """

        return (self.__size ** 2)
