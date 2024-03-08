#!/usr/bin/python3
""" Write a class that defines a square"""

class User:
    """The class defines a square"""
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an int")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size**2
