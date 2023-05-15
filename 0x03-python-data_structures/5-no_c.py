#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters 'c' and 'C' from a string."""
    copy = [x for x in my_string if x.lower() not in ['c', 'C']]
    return "".join(copy)


# Test the function

string = "Hello, World! Welcome to Python."
result = no_c(string)

print("Original string: {}".format(string))
print("String without 'c' and 'C': {}".format(result))
