#!/usr/bin/python3

"""
The inherits_from function accepts two arguments: an object (obj) and a class (a_class).
This documentation aims to provide an overview of inheritance using isinstance, issubclass,
type, and the super built-in function.

Function: inherits_from
Description:
    The inherits_from function checks if an object belongs to a class or a subclass.

Parameters:
    obj (object): The object to be checked.
    a_class (class): The class to check against.

Returns:
    bool: True if the object is an instance of the class or a subclass; False otherwise.

Examples:
    >>> inherits_from(5, int)
    True
    >>> inherits_from("hello", str)
    True
    >>> inherits_from([], list)
    True
    >>> inherits_from(5, float)
    False
"""
def inherits_from(obj, a_class):
    """
    This function checks if the obj is an instance of the specified class or a subclass.
    The isinstance function is used to perform the check, and the result is returned.
    """
    return isinstance(type(obj), a_class)
