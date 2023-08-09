#!/usr/bin/python3
'''
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
'''
class Square:
    "class Square is the blueprint to create a class and an object"
    " Additionally self, isa keyword that binds the actual value with object"
    "The self is used to initialize an object and is always called out everytme a new object is created"
    def __init__(self, size):
        self.__size = size

    "In this implementation, the __init__ method takes an optional parameter size, which is assigned to the private instance attribute __size. It performs the necessary checks to ensure that size is an integer and is greater than or equal to 0, raising appropriate exceptions if the conditions are not met."

    def __init__(self, size=0):
        if not isinstance(type(size), int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size 

    

