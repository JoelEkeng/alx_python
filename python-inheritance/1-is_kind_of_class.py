#/usr/bin/python3


"""
The is_same_class functions accepts two functions obj and a_class. 
This documentation aims to provide an overview of inheritance using isinstance, issubclas, type and super built in funciton.

Function: is_same_class
Description:
The is_same_class gets an object and check if the class corespond. 

Examples:
        # >>> is_same_class(5, int)
        True
        # >>> is_same_class("hello", str)
        True
        # >>> is_same_class([], list)
        True
        # >>> is_same_class(5, float)
        False
"""
def is_kind_of_class(obj, a_class):
    
    """
    This checks if the Obj and the classes matches.
    The isinstance function is used to check that the object matches the data type
    and returns the output.
    """
    return isinstance(obj, a_class) 
