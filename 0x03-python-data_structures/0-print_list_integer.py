#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Print all integers of a list."""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))


# Test the function

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)