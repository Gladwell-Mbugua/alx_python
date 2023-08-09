#!/usr/bin/python3
'''
Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
You are not allowed to import any module
'''
class Square:
    "class Square is the blueprint to create a class and an object"
    " Additionally self, is a keyword that binds the actual value with object"
    "The self is used to initialize an object and is always called out everytime a new object is created"
    "In this implementation, the __init__ method takes an optional parameter size, which is assigned to the private instance attribute __size. It performs the necessary checks to ensure that size is an integer and is greater than or equal to 0, raising appropriate exceptions if the conditions are not met."

    def __init__(self, size=0):
        if not isinstance(type(size), int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.size = size 

    def area(self):
        return self.size ** 2