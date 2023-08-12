#!/usr/bin/python3

"""
This module defines the Square class.

The Square class inherits from the Rectangle class.

The Square class has an area() method that calculates the area.
"""

BaseGeometry = __import__('7-rectangle').BaseGeometry


class Square(BaseGeometry):
    """
    This class defines a Square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        area(): Calculates the area of the square.

    Raises:
        AttributeError: If the attribute width or height is accessed.
        TypeError: If the value of the attribute width
        or height is not an integer.
        ValueError: If the value of the attribute width
        or height is less than or equal to 0.
    """

    def __init__(self, size):
        """
        Initializes a new square.

        Args:
            size (int): The size of the rectangle.

        Raises:
            TypeError: If the value of the attribute size is not an integer.
        """
        super().__init__()
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
        Calculates the size of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
        