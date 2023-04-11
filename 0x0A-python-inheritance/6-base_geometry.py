#!/usr/bin/python3
"""
This contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raising an exception when called"""
        raise Exception("area() is not implemented")

