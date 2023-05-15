#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return None

    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]

    return big


# Test the function
numbers = [1, 5, 3, 9, 2, 7]
result = max_integer(numbers)
print("Maximum integer:", result)
