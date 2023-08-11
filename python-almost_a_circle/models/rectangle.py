"""This module defines the Rectangle class."""

from models.base import Base

class Rectangle(Base):
    """
    Represents a geometric rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): An optional identifier for the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner. Default is 0.
            y (int, optional): The y-coordinate of the top-left corner. Default is 0.
            id (int, optional): An optional identifier for the rectangle.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        self._validate_width()
        self._validate_height()
        self._validate_x()
        self._validate_y()
    
    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, width):
        """
        Set the width of the rectangle.

        Args:
            width (int): The new width value.
        """
        if not isinstance(width, int):
           raise TypeError ('{} must be an integer'.format(width)) 
        if width <= 0:
            raise ValueError ('{} must be > 0'.format(width))
        self.__width = width

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, height):
        """
        Set the height of the rectangle.

        Args:
            height (int): The new height value.
        """
        if not isinstance(height, int):
           raise TypeError ('{} must be an integer'.format(height)) 
        if height <= 0:
            raise ValueError ('{} must be > 0'.format(height))
        self.__height = height
    
    @property
    def x(self):
        """int: The x-coordinate of the top-left corner."""
        return self.__x
    
    @x.setter
    def x(self, x):
        """
        Set the x-coordinate of the top-left corner.

        Args:
            x (int): The new x-coordinate value.
        """
        if not isinstance(x, int):
           raise TypeError ('{} must be an integer'.format(x)) 
        if x < 0:
            raise ValueError ('{} must be >= 0'.format(x))
        self.__x = x
    
    @property
    def y(self):
        """int: The y-coordinate of the top-left corner."""
        return self.__y
    
    @y.setter
    def y(self, y):
        """
        Set the y-coordinate of the top-left corner.

        Args:
            y (int): The new y-coordinate value.
        """
        if not isinstance(y, int):
           raise TypeError ('{} must be an integer'.format(y)) 
        if y < 0:
            raise ValueError ('{} must be > 0'.format(y))
        self.__y = y

    def _validate_width(self):
        """Validate the width attribute."""
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")

    def _validate_height(self):
        """Validate the height attribute."""
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")

    def _validate_x(self):
        """Validate the x attribute."""
        if not isinstance(self.__x, int):
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")

    def _validate_y(self):
        """Validate the y attribute."""
        if not isinstance(self.__y, int):
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")
