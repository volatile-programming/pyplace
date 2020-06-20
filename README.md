# pyplace (a place by percentage package)
Is easy to use package to get the placement and dimensions of a child container base on the percentage given and the relative placement and size of the parent container.

## Example:
> from pyplace.pbp import get_container, get_child_container
> 
> screen_width = 1280 <br>
> screen_height = 720
> 
> windows = get_container(parent_size:(screen_with, screen_height), percentages:(1, 1)) <br>
> upper_left_box = get_child_container(parent_container:windows, size_percentages:(0.5, 0.5)) <br>
> lower_left_box = get_child_container(parent_container:windows, size_percentages:(0.5, 0.5), place_percentages:(0,0.5)) <br>
> upper_right_box = get_child_container(parent_container:windows, size_percentages:(0.5, 0.5), place_percentages:(0.5,0)) <br>
> lower_right_box = get_child_container(parent_container:windows, size_percentages:(0.5, 0.5), place_percentages:(0.5,0.5)) <br>
