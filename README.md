# pyplace (a place by percentage package)
Is easy to use package to get the placement and dimensions of a child container base on the percentage given and the relative placement and size of the parent container.

## Example:
> from pyplace import pbp
> 
> screen_with = 1280 <br>
> screen_height = 720
> 
> windows = pbp.get_container(origin:(0, 0), parent:(screen_with, screen_height), percentage:(1, 1)) <br>
> upper_left_box = pbp.get_child_container(parent:windows, place_persentage:(0,0) size_percentage:(0.5, 0.5)) <br>
> lower_left_box = pbp.get_child_container(parent:windows, place_persentage:(0,0.5) size_percentage:(0.5, 0.5)) <br>
> upper_right_box = pbp.get_child_container(parent:windows, place_persentage:(0.5,0) size_percentage:(0.5, 0.5)) <br>
> lower_right_box = pbp.get_child_container(parent:windows, place_persentage:(0.5,0.5) size_percentage:(0.5, 0.5)) <br>
