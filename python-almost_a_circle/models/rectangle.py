from models.base import Base

class Rectangle:

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @set_width.setter
    def set_width(self, width):
        self.__width = width

    @property
    def get_width(self, width):
        return self.__width

    @set_height.setter
    def set_height(self, height):
        self.__height = height
    
    @property
    def get_height(self):
        return self.__height
    
    @set_x.setter
    def x(self, x):
        self.__x = x
    
    @property
    def get_x(self):
        return self.__x

    @set_y.setter
    def set_y(self, y):
        self.__y = y 
    
    @property
    def get_y(self):
        return self.__y
