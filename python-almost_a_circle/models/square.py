from models.rectangle import Rectangle


class Square(Rectangle):

    """
    Square class, a subclass of Rectangle.

    This class represents a square shape and inherits attributes and methods
    from the Rectangle class. It adds an additional 'size' attribute to the
    Square objects.

    Attributes:
    - id (int): A unique identifier for the Square.
    - x (int): The x-coordinate of the top-left corner of the Square.
    - y (int): The y-coordinate of the top-left corner of the Square.
    - size (int): The side length of the Square.

    Methods:
    - __init__(self, size, x=0, y=0, id=None): Constructor to initialize a Square object.
    - __str__(self): Return a formatted string representation of the Square object.

    Note: This class assumes that the Rectangle class is defined in 'models.rectangle'.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Parameters:
        size (int): The side length of the square.
        x (int): The x-coordinate of the top-left corner of the square. Default is 0.
        y (int): The y-coordinate of the top-left corner of the square. Default is 0.
        id (int): A unique identifier for the square. Default is None.

        Note: The constructor initializes attributes 'id', 'x', 'y', and 'size'.
        """
        super().__init__(id, x, y, width, height)
        self.size = width
        self.size = height
    
    def __str__(self):
        """
        Generate a formatted string representation of the Square.

        Returns:
        str: A formatted string representing the Square object.
        """
        return ('[Square] ({}) <{}>/<{}> - <{}>'.format(self.id, self.x, self.y, self.size))
