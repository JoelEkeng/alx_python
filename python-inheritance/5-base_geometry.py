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
    def __dir__(cls):
        """This is used to check the list of attributes in the dir magic class.
        It ensures that __init_subclass__ is not printed"""
        return [attribute for attribute in super.__dir__() if attribute != '__init_subclass__']
class BaseGeometry(metaclass=BaseGeometrymetaclass):
    """This is an empty class.
    The Pass keyword is used to print an empty line
    """
    pass

    def __dir__(cls):
        """This is used to check the list of attributes in the dir magic class.
        It ensures that __init_subclass__ is not printed"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def area(self):
        """It's used to raise an exception that the area method is not implemented
        """
        raise Exception ('area() is not implemented')

    def integer_validator(self, name, value):
        """Creating an instance of name and value
        """
        self.name = name
        self.value = value
        
        """Checking that the value passed by the user is an Integer
        If it's not an Integer, a TypeError is raised
        """
        if not isinstance(int, value):
            raise TypeError ('{} must be an integer'.format(value))
        """Checking that the value must be great than zero
        if the value is less than or equal to zero, then a valueError is raised.
        """
        if value <= 0 :
            raise ValueError ('{} must be greater than 0'.format(value))
