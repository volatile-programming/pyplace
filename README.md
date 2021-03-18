# pyplace (a place by percentage Python package)

### _Full definition:_

Pyplace is a easy to use package to get the placement and dimensions of a child container base on the percentage given the size of a parent container and/or the relative origin of the child and parent containers.

### _In a few words definition:_

A littler utility to stop remembering tons of numbers and star using percentages for containers size and placement.

## Usage

```python
from pyplace.pbd import *
```

Is the main package module it contains two methods _get_container()_ and _get_child_container()_ witch will be described in more details down below:

**get_container(parent_size: tuple, percentages: tuple, origin: tuple = None)**

```python
"""
    Gets a new parent container base on the size and percentages given.

    Args:
        parent_size: The width and height size reference for the new parent container.
        percentages: The width and height percentages to get the size for the new parent container.
        (optional)  origin: The x and y coordinates to place the new parent container.

    Raises:
    TypeError: If an argument variable was not send as a tuple.

    Returns:
    A Container class with the x, y, width and height values for the new parent container.
"""
```

**get_child_container(parent_container: Container, size_percentages: tuple, place_percentages: tuple = (0,0))**

```python
"""
    Gets a new child container base on the parent container and size percentages given.

    Args:
        parent_container: The x, y, width and height value of the child container.
        size_percentages: The width and height percentages to get the size for the new child container.
        (optional)  place_percentages: The x and y percentages to get the placement for the new child container.

    Raises:
    TypeError: If an argument variable was not send as a tuple.

    Returns:
    A Container class with the x, y, width and height values for the new child container.
```

### Example:

```python
    # full screen window with a window container and four child containers.
    from pyplace.pbp import get_container, get_child_container

    # we assume the display resolution is 1280x720 for this example.
    import pyautogui
    # Returns: tuple(1280, 720)
    screen_width, screen_height = pyautogui.size()

    window = get_container(parent_size=(screen_with, screen_height), percentages=(1, 1))
    # Returns: tuple(0, 0, 1280, 720)
    window.get_dimensions()

    upper_left_box = get_child_container(parent_container=window, size_percentages=(0.5, 0.5))
    # Returns: tuple(0, 0, 640, 360)
    upper_left_box.get_dimensions()

    lower_left_box = get_child_container(parent_container=window, size_percentages=(0.5, 0.5), place_percentages=(0, 0.5))
    # Returns: tuple(0, 360, 640, 360)
    lower_left_box.get_dimensions()

    upper_right_box = get_child_container(parent_container=window, size_percentages=(0.5, 0.5), place_percentages=(0.5, 0))
    # Returns: tuple(640, 0, 640, 360)
    upper_right_box.get_dimensions()

    lower_right_box = get_child_container(parent_container=window, size_percentages=(0.5, 0.5), place_percentages=(0.5, 0.5))
    # Returns: tuple(640, 360, 640, 360)
    lower_right_box.get_dimensions()
```

> This is just litter demonstrations of all the possibles configurations for size and placement.

## Container

when we call the _get_container_ or _get_child_container_ we get a Container instance that we can use for getting a tuple of single variables holding the size and placement information for the container we created.

here are the attributes and method we get on this class:

```python
"""
    # attribute list.
    __x       # the container x position.
    __y       # the container x position.
    __width   # the container width dimension.
    __height  # the container height dimension.

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

    get_dimensions()                    # returns a tuple with the x, y, width and height of the container.
    set_dimensions(x: int, y: int, width: int, height: int)  # sets the x, y, width and height of the container.
"""
```
