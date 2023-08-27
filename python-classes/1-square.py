#!/usr/bin/python3
class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square's sides.

    Methods:
        __init__(self, size=0): Initializes a new square instance with a given size.

    """
    def __init__(self, size=0):
        """
        Initializes a new square instance with a given size.

        Args:
            size (int): The size of the square's sides. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
