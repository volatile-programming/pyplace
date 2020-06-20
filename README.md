# pyplace (a place by percentage package)
Is easy to use package to get the placement and dimensions of a child container base on the percentage given and the relative placement and size of the parent container.

## pdb
Is the main package module it contains two methods *get_container* and *get_child_container* witch will be descrived in more ditails down here.

    # Gets a new parent container base on the size and percentages given.
    get_container(parent_size: tuple, percentages: tuple, origin: tuple = None)
    # Args:
    #                parent_size: The width and height size reference for the new parent container.
    #                percentages: The width and height percentages to get the size for the new parent container.
    #    (optional)  origin: The x and y cordinates to place the new parent container.
    #
    # Raises:
    #    TypeError: If an argument variable was not send as a tuple.
    #    
    # Returns:
    #    A Container class with the x, y, width and height values for the new parent container.
    
    # Gets a new child container base on the parent container and size percentagesgiven.
    get_child_container(parent_container: Container, size_percentages: tuple, place_percentages: tuple = (0,0))
        # Args:
        #                parent_container: The x, y, width and height value of the child container.
        #                size_percentages: The width and height percentages to get the size for the new child container.
        #    (optional)  place_percentages: The x and y percentages to get the placement for the new child container.
        # 
        # Raises:
        #    TypeError: If an argument variable was not send as a tuple.
        #
        # Returns:
        #    A Container class with the x, y, width and height values for the new child container.

## Example:

    # full screen window with four child boxes
    from pyplace.pbp import get_container, get_child_container

    screen_width = 1280 <br>
    screen_height = 720

    window = get_container(parent_size=(screen_with, screen_height), percentages=(1, 1)) <br>
    window.get_dimentions() #(0, 0, 1280, 720)

    upper_left_box = get_child_container(parent_container=window, size_percentages=(0.5, 0.5)) <br>
    upper_left_box.get_dimentions() #(0, 0, 640, 360)

    lower_left_box = get_child_container(parent_container=window, size_percentages=(0.5, 0.5), place_percentages=(0, 0.5)) <br>
    lower_left_box.get_dimentions() #(0, 360, 640, 360)

    upper_right_box = get_child_container(parent_container=window, size_percentages=(0.5, 0.5), place_percentages=(0.5, 0)) <br>
    upper_right_box.get_dimentions() #(640, 0, 640, 360)

    lower_right_box = get_child_container(parent_container=window, size_percentages=(0.5, 0.5), place_percentages=(0.5, 0.5)) <br>
    lower_right_box.get_dimentions() #(640, 360, 640, 360)


## Container
when we call the *get_container* or *get_child_container* we get a Container instance that we can use for getting a tuple of single variables holding the size and placement information for the container we created.

here are the attributes and method we get on this class:

    # atribute list.
    __x       # the container x position.
    __y       # the container x position.
    __width   # the container width dimention.
    __height  # the container height dimention.

    # method list.
    get_x()                             # returns the x value for the container.
    set_x(x: int)                       # sets the x value for the container.

    get_y()                             # returns the y value for the container.
    set_y(y: int)                       # sets the y value for the container.

    get_placement()                     # returns a tuple with the x and y of the container.
    set_placement(x: int, y: int)       # sets the x and y of the container.

    get_width()                         # returns the width value for the container.
    set_width(width: int)               # sets the width value for the container.

    get_height()                        # returns the height value for the container.
    set_height(height: int)             # sets the height value for the container.

    get_size()                          # returns a tuple with the width and height of the container.
    set_size(width: int, height: int)   # sets the width and height of the container.

    get_dimentions()                    # returns a tuple with the x, y, width and height of the container.
    set_dimentions(x: int, y: int, width: int, height: int)  # sets the x, y, width and height of the container.
