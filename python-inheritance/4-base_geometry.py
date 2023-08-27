#!/usr/bin/env/python3
"""
Write a class BaseGeometry (based on 3-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
You are not allowed to import any module
"""
class BaseGeometry:
    """
    A base geometry class.
    """

    def area(self):
        """
        Raises an exception indicating that the method is not implemented.

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
