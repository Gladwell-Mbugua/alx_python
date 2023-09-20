#!/usr/bin/env/python3
"""
This is a base class for custom metaclass TypeMetaClass.
"""

class TypeMetaClass(type):
    """
    This is a metaclass used to represent the class type in order to eliminate
    the inherited method init subclass.
    """
    def __dir__(cls) -> None:
        """
        Exclude attribute init subclass in dir().
        """
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']

class BaseGeometry(metaclass=TypeMetaClass):
    """
    This is a base class that uses the custom metaclass TypeMetaClass to exclude
    the __init_subclass__ attribute from the list of attributes returned by dir().
    """
    def __init__(self):
        pass
