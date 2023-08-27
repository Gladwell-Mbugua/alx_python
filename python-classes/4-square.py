#!/usr/bin/python3
'''
mandatory
Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
You are not allowed to import any module
'''

class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square's sides.

    Methods:
        __init__(self, size=0): Initializes a new square instance with a given size.
        area(self): Returns the current square area.
        my_print(self): Prints the square with the character #.

    Properties:
        size(self): Retrieves the size of the square.
        size(self, value): Sets the size of the square.

    Usage:
        To create a square instance, provide the size of the sides as an argument to the constructor.
        Example:
        >>> square1 = Square(5)  # Creates a square with sides of size 5

        If no size is provided, the default size is 0.
        Example:
        >>> square2 = Square()   # Creates a square with default size 0

        Note:
        The size must be a non-negative integer value. Otherwise, exceptions will be raised.
    """

    def __init__(self, size=0):
        """
        Initializes a new square instance with a given size.

        Args:
            size (int): The size of the square's sides. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Usage:
            To create a square instance, provide the size of the sides as an argument.
            Example:
            >>> square = Square(5)  # Creates a square with sides of size 5

            If no size is provided, the default size is 0.
            Example:
            >>> square = Square()   # Creates a square with default size 0

            Note:
            The size must be a non-negative integer value. Otherwise, exceptions will be raised.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
