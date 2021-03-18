"""container.py:
    A module with a container class that holds variables and methdos
    helpful for storing/retrieving positional (x, y) and dimensional (width, height) data.

    Version:  0.6.8
    Author:  Jeffrey Issaul Jose de la Rosa.
"""

class Container:
    """A Size/Placement holder with some getters and setters to work with its attributes."""
    def __init__(self, x: int, y: int, width: int, height: int):
        self.set_x(x)
        self.set_y(y)
        self.set_width(width)
        self.set_height(height)

    def get_x(self) -> int:
        return self.__x

    def set_x(self, x: int):
        self.__x = x

    def get_y(self) -> int:
        return self.__y

    def set_y(self, y: int):
        self.__y = y
       
    def get_placement(self) -> tuple:
        return (self.__x, self.__y)
    
    def set_placement(self, x: int, y: int):
        self.set_x(x)
        self.set_y(y)

    def get_width(self) -> int:
        return self.__width

    def set_width(self, width: int):
        self.__width = width if width else 0

    def get_height(self) -> int:
        return self.__height

    def set_height(self, height: int):
        self.__height = height if height else 0

    def get_size(self) -> tuple:
        return (self.__width, self.__height)
    
    def set_size(self, width: int, height: int):
        self.set_width(width)
        self.set_height(height)

    def get_dimensions(self) -> tuple:
        return (self.__x, self.__y, self.__width, self.__height)

    def set_dimensions(self, x: int, y: int, width: int, height: int):
        self.set_placement(x, y)
        self.set_size(width, height)
