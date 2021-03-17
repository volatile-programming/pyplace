"""pbp.py:
    pbp :=> (Place by Percentage)
    A module to get the size and placement of a child container in relation with
    the percentage to be taken from the parent container's size and placement.

    Version: 0.6.0
    Author:  Jeffrey Issaul Jose de la Rosa.

Usage:

    from pbp import get_container, get_child_container
"""
import math

from container import Container

def get_container(parent_size: tuple, percentages: tuple, origin: tuple = None) -> Container:
    """Gets a new parent container base on the size and percentages given.

    Args:
                    parent_size: The width and height size reference for the new parent container.
                    percentages: The width and height percentages to get the size for the new parent container.
        (optional)  origin: The x and y coordinates to place the new parent container.
    
    Raises:
        TypeError: If an argument variable was not send as a tuple.
        
    Returns:
        A Container class with the x, y, width and height values for the new parent container.
    """
    origin_x = 0
    origin_y = 0
    parent_width = 0
    parent_height = 0
    vertical_percentage = 0
    horizontal_percentage = 0

    try:
        if origin is not None:
            origin_x, origin_y = origin
        parent_width, parent_height = parent_size
        vertical_percentage, horizontal_percentage = percentages
    except(TypeError) as e:
        raise e

    width  = int(math.floor(parent_width * vertical_percentage))
    height = int(math.floor(parent_height * horizontal_percentage))

    return Container(origin_x, origin_y, width, height)

def get_child_container(parent_container: Container, size_percentages: tuple, place_percentages: tuple = (0,0)) -> Container:
    """Gets a new child container base on the parent container and size percentages given.

    Args:
                    parent_container: The x, y, width and height value of the parent container.
                    size_percentages: The width and height percentages to get the size for the new child container.
        (optional)  place_percentages: The x and y percentages to get the placement for the new child container.

    Raises:
        TypeError: If an argument variable was not send as a tuple.
    
    Returns:
        A Container class with the x, y, width and height values for the new child container.
    """
    parent_x = 0
    parent_y = 0
    parent_width = 0
    parent_height = 0
    vertical_size_percentage = 0
    horizontal_size_percentage = 0
    vertical_place_percentage = 0
    horizontal_place_percentage = 0

    try:
        parent_x, parent_y, parent_width, parent_height = parent_container.get_dimensions()

        vertical_size_percentage, horizontal_size_percentage = size_percentages
        vertical_place_percentage, horizontal_place_percentage = place_percentages
    except(TypeError) as e:
        raise e

    origin_x = int(math.floor(parent_x + (parent_width * vertical_place_percentage)))
    origin_y = int(math.floor(parent_y + (parent_height * horizontal_place_percentage)))
    width  = int(math.floor(parent_width * vertical_size_percentage))
    height = int(math.floor(parent_height * horizontal_size_percentage))

    return Container(origin_x, origin_y, width, height)
