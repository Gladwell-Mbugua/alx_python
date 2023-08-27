#!/usr/bin/env/python3
"""
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

Prototype: def is_kind_of_class(obj, a_class):
You are not allowed to import any module
"""
def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or an instance of a class that inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class or its subclasses, otherwise False.
    """
    return isinstance(obj, a_class)
