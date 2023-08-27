#!/usr/bin/env/python3
"""
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
You are not allowed to import any module
"""
def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class, otherwise False.
    """
    return type(obj) is a_class
