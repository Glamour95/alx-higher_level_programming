###Project Name
###Exception Handling Functions

###Description

***This project contains several functions for handling exceptions in Python. Each function focuses on a specific task, such as printing elements of a list, printing integers, dividing numbers, and raising exceptions.

###Table of Contents
###Installation

Usage

###Functions

***Safe Print List
***Safe Print Integer
***Safe Print List Integers
***Safe Print Division
***List Division
***Raise Exception
***Raise Exception with Message
***Contributing

###License
###Installation

***To use these functions, follow these steps:

***Navigate to the project directory: cd alx-higher_level_programming/0x05-python-exceptions

###Usage
***Each function can be used independently in your Python program. You can import the desired function from its corresponding file into your code.

****from 0-safe_print_list import safe_print_list

**my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))

###Functions

***Safe Print List

###Prototype: def safe_print_list(my_list=[], x=0)

my_list can contain elements of any type (integer, string, etc.).
Prints x elements of the list on the same line, followed by a new line.
If x is larger than the length of my_list, it prints all the elements of my_list.
Returns the actual number of elements printed.

***Uses try and except for exception handling.
Does not import any modules.
Does not use len().

Safe Print Integer

###Prototype: def safe_print_integer(value)

value can be any type (integer, string, etc.).
Prints the integer value followed by a new line using the format "{:d}".
Returns True if the value is an integer and has been printed correctly.
Returns False if the value is not an integer.
Uses try and except for exception handling.
Does not import any modules.
Does not use type().

Safe Print List Integers

###Prototype: def safe_print_list_integers(my_list=[], x=0)

my_list can contain elements of any type (integer, string, etc.).
Prints only the integers in my_list on the same line, followed by a new line.
Skips other types of values in the list without printing.
Prints at most x integers from the list.
Returns the actual number of integers printed.
Uses try and except for exception handling.
Uses "{:d}" format to print integers.
Does not import any modules.
Does not use len().
Safe Print Division

###Prototype: def safe_print_division(a, b)

Divides two integers, a and b.
Prints the result of the division preceded by "Inside result:" in the finally section.
Returns the value of the division.
Uses try, except, and finally for exception handling.
Uses "{:d}".format() to print the result as a string.

Does not import any modules.
List Division

###Prototype: def list_division(my_list_1, my_list_2, list_length)

Divides the elements of my_list_1 by the corresponding elements in my_list_2.
my_list_1 and my_list_2 can contain elements of any type (integer, string, etc.).
The resulting list will have a length of list_length.
If an element in either list cannot be divided, the division result for that element will be 0.
If an element is not an integer or float, it prints "wrong type".
If the division by 0 occurs, it prints "division by 0".
If my_list_1 or my_list_2 is too short to perform the division for list_length elements, it prints "out of range".

Uses try, except, and finally for exception handling.
Does not import any modules.
Raise Exception

###Prototype: def raise_exception()

Raises a type exception.
Does not import any modules.
Raise Exception with Message

###Prototype: def raise_exception_msg(message="")

Raises a name exception with a custom message.
message is an optional parameter to specify the custom message.
Does not import any modules.
Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvement, feel free to create a pull request.

###License
This project is licensed under the MIT License.

#endif
