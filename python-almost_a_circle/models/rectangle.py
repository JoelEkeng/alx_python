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
        self.__y = y
