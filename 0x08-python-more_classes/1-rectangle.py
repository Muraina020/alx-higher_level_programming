#!/usr/bin/python3
"""Gives a definition of a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width = 0, height = 0):
        """Do the initialization of a new Rectangle.
        Args:
            width (int): Represent the width of the new rectangle.
            height (int): Represent the height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

