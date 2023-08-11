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
        return [attribute for attribute in super.__dir__() if attribute != '__getstate__']

class BaseGeometry(metaclass=BaseGeometrymetaclass):
    """This is an empty class.
    The Pass keyword is used to print an empty line
    """
    pass

    def __dir__(cls):
        """This is used to check the list of attributes in the dir magic class.
        It ensures that __init_subclass__ is not printed"""
        return [attribute for attribute in super().__dir__() if attribute != '__getstate__']

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
        if not isinstance(value, int):
            raise TypeError ('{} must be an integer'.format(name))
        """Checking that the value must be great than zero
        if the value is less than or equal to zero, then a valueError is raised.
        """
        if value <= 0 :
            raise ValueError ('{} must be greater than 0'.format(name))

class Rectangle(BaseGeometry):
    """
    The Rectangle class inherits from the BaseGeometry class
    """
    def __init__(self, width, height):
        """
          Initializes a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If the value of the attribute width or height is not an integer.
            ValueError: If the value of the attribute width or height is less than or equal to 0.
        """
        BaseGeometry.integer_validator()
        # self.integer_validator("width", width)
        # self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    # def area(self):
    #     """
    #     Calculates the area of the rectangle.

    #     Returns:
    #         int: The area of the rectangle.
    #     """
    #     return self.__width * self.__height

    # def __getattribute__(self, name):
    #     if name in ["_width", "_height"]:
    #         raise AttributeError("'Rectangle' object has no attribute '{}'".format(name))
    #     elif name == "height" and not isinstance(object.__getattribute__(self, "_height"), int):
    #         raise TypeError("height must be an integer")
    #     return super().__getattribute__(name)

    def __dir__(cls):
        """This is used to check the list of attributes in the dir magic class.
        It ensures that __init_subclass__ is not printed"""
        return [attribute for attribute in super().__dir__() if attribute != '__getstate__']
