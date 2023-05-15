#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list


# Test the function
my_list = [1, 2, 3, 4, 5]
index = 2
new_element = 10
result = replace_in_list(my_list, index, new_element)
print("Updated list:", result)
