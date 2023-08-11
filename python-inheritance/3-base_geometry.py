#!/usr/bin/python3

"""
3-base_geometry
It contains an empty class call BaseGeometry

"""
class BaseGeometrymetaclass(type):
    """
        This is a meta class created to inform the behaviour of the BaseGeometry class.
        It's the base class for the BaseGeometry class
    """
    def __new__(cls, name, bases, attrs):
        #customize the class creation process here
        return super().__new__(cls, name, bases, attrs)

    def __dir__(cls):
        """This is used to check the list of attributes in the dir magic class.
        It ensures that __init_subclass__ is not printed"""
        return [attribute for attribute in super.__dir__() if attribute != '__init_subclass__']
class BaseGeometry(BaseGeometrymetaclass('BaseGeometry', (), {})):
    """This is an empty class.
    The Pass keyword is used to print an empty line
    """
    pass

    def __dir__(cls):
        """This is used to check the list of attributes in the dir magic class.
        It ensures that __init_subclass__ is not printed"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
