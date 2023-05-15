#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    copy = [x for x in my_list]
    copy[idx] = element
    return copy

# Test the function

my_list = [1, 2, 3, 4, 5]
index = 2
new_element = 10
result = new_in_list(my_list, index, new_element)
print("Original list:", my_list)
print("New list:", result)
