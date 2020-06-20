"""pbp.py:
    pbp :=> (Place by Percentage)
    A module to get the size and placement of a chaild container in relation with
    the percentage to be taken from the parent container's size and placement.

    Version: 0.4.0
    Autor:  Jeffrey Issaul Jose de la Rosa.
"""
import math

from container import Container

def get_container(parent_size, percentages, origin=None):
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

def get_child_container(parent_container, size_percentages, place_percentages):
    parent_x = 0
    parent_y = 0
    parent_width = 0
    parent_height = 0
    vertical_size_percentage = 0
    horizontal_size_percentage = 0
    vertical_place_percentage = 0
    horizontal_place_percentage = 0

    try:
        parent_x = parent_container.x
        parent_y = parent_container.y
        parent_width = parent_container.width
        parent_height = parent_container.height

        vertical_size_percentage, horizontal_size_percentage = size_percentages
        vertical_place_percentage, horizontal_place_percentage = place_percentages
    except(TypeError) as e:
        raise e

    origin_x = int(math.floor(parent_x + (parent_width * vertical_place_percentage)))
    origin_y = int(math.floor(parent_y + (parent_height * horizontal_place_percentage)))
    width  = int(math.floor(parent_width * vertical_size_percentage))
    height = int(math.floor(parent_height * horizontal_size_percentage))

    return Container(origin_x, origin_y, width, height)
