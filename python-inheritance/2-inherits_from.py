#!/usr/bin/env/python3
"""
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

Prototype: def inherits_from(obj, a_class):
You are not allowed to import any module
"""
def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object's class inherits from the specified class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
