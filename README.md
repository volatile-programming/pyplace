# pyplace (a place by percentage package)
Is easy to use package to get the placement and dimensions of a child container base on the percentage given and the relative placement and size of the parent container.

## Example:
> from pyplace.pbp import get_container, get_child_container
> 
> screen_width = 1280 <br>
> screen_height = 720
> 
> windows = get_container(parent_size:(screen_with, screen_height), percentages:(1, 1)) <br>
> windows.get_dimentions() #(0, 0, 1280, 720)
> 
> upper_left_box = get_child_container(parent_container:windows, size_percentages:(0.5, 0.5)) <br>
> upper_left_box.get_dimentions() #(0, 0, 640, 360)
> 
> lower_left_box = get_child_container(parent_container:windows, size_percentages:(0.5, 0.5), place_percentages:(0, 0.5)) <br>
> lower_left_box.get_dimentions() #(0, 360, 640, 360)
> 
> upper_right_box = get_child_container(parent_container:windows, size_percentages:(0.5, 0.5), place_percentages:(0.5, 0)) <br>
> upper_right_box.get_dimentions() #(640, 0, 640, 360)
> 
> lower_right_box = get_child_container(parent_container:windows, size_percentages:(0.5, 0.5), place_percentages:(0.5, 0.5)) <br>
> lower_right_box.get_dimentions() #(640, 360, 640, 360)


## Container
when we call the *get_container* or *get_child_container* we get a Container instance that we can use for getting a tupple of single variables holding the size and placement information for the container we created.

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

    get_placement()                     # returns a tupple with the x and y of the container.
    set_placement(x: int, y: int)       # sets the x and y of the container.

    get_width()                         # returns the width value for the container.
    set_width(width: int)               # sets the width value for the container.

    get_height()                        # returns the height value for the container.
    set_height(height: int)             # sets the height value for the container.

    get_size()                          # returns a tupple with the width and height of the container.
    set_size(width: int, height: int)   # sets the width and height of the container.

    get_dimentions()                                         # returns a tupple with the x, y, width and height of the container.
    set_dimentions(x: int, y: int, width: int, height: int)  # sets the x, y, width and height of the container.
