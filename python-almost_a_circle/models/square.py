from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width, height)
        self.size = width
        self.size = height
    
    def __str__(self):
        return ('[Square] ({}) <{}>/<{}> - <{}>'.format(self.id, self.x, self.y, self.size))
