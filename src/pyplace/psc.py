"""psc.py: psc => (Placement and Size Container)

    A module with a container class that holds variables and methdos helpful for storing and retrieving positional (x, y) and dimensional (width, height) data.
"""

class PlacementAndSizeContainer:
    """
    A class used to hold the Size and Placement of a object

    Attributes
    ----------
    __x: int
        a rounded-down int that holds the x position of the object.
    __y: int
        a rounded-down int that holds the y position of the object.
    __width: int
        a rounded-down int that holds the width size of the object.
    __height: int
        a rounded-down int that holds the height size of the object.

    Methods
    -------
    (Getters):
        get_x(int) -> int
            returns a int with the current value of the __x attribute.
        get_y(int) -> int
            returns a int with the current value of the __y attribute.
        get_width(int) -> int
            returns a int with the current value of the __width attribute.
        get_height(int) -> int
            returns a int with the current value of the __height attribute.
        get_placement(int,int) -> tuple(int,int)
            returns a tuple with the current values of the __x and __y attributes.
        get_size(int,int) -> tuple(int,int)
            returns a tuple with the current values of the __width and __height attributes.
        get_dimensions(int,int,int,int) -> tuple(int,int,int,int)
            returns a tuple with the current values of the __x, __y, __width and __height attributes.

    (Setters):
        x(int)
            sets the value of the __x attribute.
        y(int)
            sets the value of the __y attribute.
        width(int)
            sets the value of the __width attribute.
        height(int)
            sets the value of the __height attribute.
        placement(int,int)
            sets the values of the __x and __y attributes.
        size(int,int)
            sets the values of the __width and __height attributes.
        dimensions(int,int,int,int)
            sets the values of the __x, __y, __width and __height attributes.
    """

    def __init__(self, x: int, y: int, width: int, height: int):
        """
        Parameters
        ----------
        x : int
            The x position of the object
        y : int
            The y position of the object
        width : int
            The width size of the object
        height : int
            The height size of the object
        """

        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    @property
    def x(self) -> int:
        """get_x() -> int: # sets the __x attribute of the class."""
        return self.__x

    @property.setter
    def x(self, x: int):
        """x(x: int): # gets the __x attribute of the class."""
        self.__x = x

    @property
    def y(self) -> int:
        """get_y() -> int: # gets the __y attribute of the class."""
        return self.__y

    @property.setter
    def y(self, y: int):
        """y(y: int): # sets the __y attribute of the class."""
        self.__y = y

    def get_placement(self) -> tuple:
        """get_placement() -> tuple: # gets the __x and __y attributes of the class."""
        return (self.x, self.y)

    def set_placement(self, x: int, y: int):
        """set_placement(x: int, y: int) -> tuple: # sets the __x and __y attributes of the class."""
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        """width() -> int: # gets the __width attribute of the class."""
        return self.__width

    @property.setter
    def width(self, width: int):
        """width(width: int): # sets the __width attribute of the class."""
        self.__width = width if width >= 0 else -width

    @property
    def height(self) -> int:
        """height() -> int: # gets the __height attribute of the class."""
        return self.__height

    @property.setter
    def height(self, height: int):
        """height(height: int): # sets the __height attribute of the class."""
        self.__height = height if height >= 0 else -height

    def get_size(self) -> tuple:
        """get_size() -> tuple: # gets the __width and __height attributes of the class."""
        return (self.width, self.height)

    def set_size(self, width: int, height: int):
        """set_size(width: int, height: int) -> tuple: # sets the __width and __height attributes of the class."""
        self.width = width
        self.height = height

    def get_dimensions(self) -> tuple:
        """get_dimensions() -> tuple: # gets the __x, __y, __width and __height attributes of the class."""
        return (self.x, self.y, self.width, self.height)

    def set_dimensions(self, x: int, y: int, width: int, height: int):
        """get_dimensions(x: int, y: width: int, height: int) -> tuple: # sets the __x, __y, __width and __height attributes of the class."""
        self.placement(x, y)
        self.size(width, height)
