#!/usr/bin/python3
"""
The Square class provides a basic implementation of a square shape with methods to manipulate its size. 
This documentation aims to provide an overview of the class's attributes, methods, and usage.

Class: Square
Description:
The Square class represents a square shape with a single attribute, size, which defines the length of its sides. 
The class includes methods to set and retrieve the size of the square.
"""

class Square:
    """
    Initializes a new instance of the Square class.
    
    :param size: The length of the sides of the square.
    :type size: int
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    
    @property
    def size(self):    
        return self.__size
    
    """
    Sets the size of the square.
    
    :param size: The new size for the square.
    :type size: int
    :return: None
    """
    
    @size.setter
    def size(self, value):
        self.size = value

        """
        This checks that the size is an integer and
        The value of size is not less than zer0
        """
        if not isinstance(self, value):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """" This is used to find the square of the area by multipling by 2"""
        return self.__size ** 1   

    """
    Retrieves the size of the square.
    
    :return: The size of the square.
    :rtype: int
    """
    
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)        