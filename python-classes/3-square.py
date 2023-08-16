#!/usr/bin/python3
'''
Write a class Square that defines a square by: (based on 2-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
You are not allowed to import any module
'''

class Square:
    "class Square is the blueprint to create a class and an object"
    " Additionally self, is a keyword that binds the actual value with object"
    "The self is used to initialize an object and is always called out everytime a new object is created"
    "In this implementation, the __init__ method takes an optional parameter size, which is assigned to the private instance attribute __size. It performs the necessary checks to ensure that size is an integer and is greater than or equal to 0, raising appropriate exceptions if the conditions are not met."

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value)is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must ba >= 0")
        else:
            self.__size = value

    def area(self):
        return self.size **2




   