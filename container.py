"""container.py:
    container :=> (placement holder with some getters and setters)
    A module with a container class that holds variables and methdos
    helpful for storing positional (x, y) and dimentional (width, height) data.

    Version: 0.4.0
    Autor:  Jeffrey Issaul Jose de la Rosa.
"""

class Container:
    def __init__(self, x, y, width, height):
        self.set_x(x)
        self.set_y(y)
        self.set_width(width)
        self.set_height(height)
    
    def get_dimentions(self):
        return (self.__x, self.__y, self.__width, self.__height)

    def set_dimentions(self, x, y, width, height):
        self.set_x(x)
        self.set_y(y)
        self.set_width(width)
        self.set_height(height)
    
    def get_placement(self):
        return (self.__x, self.__y)
    
    def set_placement(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def get_size(self):
        return (self.__width, self.__height)
    
    def set_size(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width if width else 0

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height if height else 0
