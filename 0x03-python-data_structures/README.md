### Python - Data Structures: Lists, Tuples

### This project, developed by Glamour, focuses on understanding and utilizing sequence data types in Python, specifically lists and tuples.

### Tests :heavy_check_mark:
tests: This folder contains the test files provided by ALX School.

### Function Prototypes :floppy_disk:
### The project includes various functions, each with its own prototype:

| File    				| Prototype                          	   	        |
|0-print_list_integer.py 		| def print_list_integer(my_list=[]): 	                |
|1-element_at.py			| def element_at(my_list, idx):                         |
|2-replace_in_list.py    		| def replace_in_list(my_list, idx, element):           |
|3-print_reversed_list_integer.py       | def print_reversed_list_integer(my_list=[]):          |
|4-new_in_list.py                       | def new_in_list(my_list, idx, element):		|
|5-no_c.py    				| def no_c(my_string):                                  |
|6-print_matrix_integer.py       	| def print_matrix_integer(matrix=[[]]):	        |
|7-add_tuple.py  			| def add_tuple(tuple_a=(), tuple_b=()):	        |
|8-multiple_returns.py   		| def multiple_returns(sentence):                       |
|9-max_integer.py       		| def max_integer(my_list=[]):			        |
|10-divisible_by_2.py    		| def divisible_by_2(my_list=[]):		        |
|11-delete_at.py 			| def delete_at(my_list=[], idx=0):		        |
|100-print_python_list_info.c    	| void print_python_list_info(PyObject *p);	        |


### Tasks :page_with_curl:
### The project consists of the following tasks:


***0. Print a list of integers

***0-print_list_integer.py: 
***This Python function prints all integers of a list, with each integer on a separate line.
***It achieves this without importing modules or casting integers into strings.


***1. Secure access to an element in a list

***1-element_at.py: 
***This Python function retrieves an element from a list.
***If idx is negative or out of range (greater than the number of elements in
***my_list), the function returns None.
***It accomplishes this without importing modules or using try/except.

***2. Replace element

***2-replace_in_list.py: 
***This Python function replaces an elementof a list at a specific position.
***If idx is negative or out of range (greater than the number of elements
in my_list), the function returns the original list.
***It achieves this without importing modules or using try/except.

***3. Print a list of integers... in reverse!

***3-print_reversed_list_integer.py:

***This Pythonfunction prints all integers of a list, with each integer on a separate line, in reverse order.
***It does so without importing modules or casting integers into strings.

***4. Replace in a copy

***4-new_in_list.py: This Python function replaces an element of a
***list at a specific position without modifying the original list.
***If `idx is negative or out of range (greater than the number of elements in
***my_list), the function returns the original list.
***It accomplishes this without importing modules or using try/except.


***5. Can you C me now?

***5-no_c.py: This Python function removes all occurrences of the characters 'c'
and 'C' from a string and returns the modified string.
***It does so without importing modules or using the str.replace() function.


***6. Lists of lists = Matrix

***6-print_matrix_integer.py: This Python function prints
a matrix of integers, with each row on a separate line.
***It achieves this without casting integers into strings.


***7. Tuples addition

***7-add_tuple.py: This Python function adds two tuples and returns a new tuple.
***The resulting tuple contains two integers:
***The first element is the sum of the corresponding elements from both tuples.
***The second element is the sum of the second elements from both tuples.
***If a tuple has fewer than 2 elements, the value 0 is used for the missing integer.
***If a tuple has more than 2 elements, only the first two integers are considered.
***It does not require importing any modules.

***8. More returns!

***8-multiple_returns.py: This Python function returns a tuple
containing the length of a string and its first character.
***If the string is empty, the first character in the tuple is set to None.
***It accomplishes this without importing any modules.

***9. Find the max

***9-max_integer.py: This Python function finds the maximum integer
in a list.
***If the list is empty, the function returns None.
***It does not require importing any modules or using the built-in max() function.

***10. Only by 2

***10-divisible_by_2.py: This Python function finds all multiples
of 2 in a list and returns a new list.
***The resulting list has the same size as the original list. Each element in the new list
is either True or False, indicating whether the corresponding integer in the original list
is divisible by 2.
***It accomplishes this without importing any modules.


***11. Delete at

***11-delete_at.py: This Python function deletes an item at
a specific position in a list.
***If idx is negative or out of range (greater than or equal to the number of elements in
my_list), the function returns the original list.
***It does not require importing any modules or using the pop() function.


***12. Switch

***12-switch.py: This Python program switches the values of variables a and b.
It completes this source code.


***13. Linked list palindrome

***13-is_palindrome.c: This C function checks if a
singly-linked list is a palindrome.
***If the function determines that the list is a palindrome, it returns 1.
***If the function determines that the list is not a palindrome, it returns 0.
***An empty list is considered a palindrome.
***The project includes helper files:
***linked_lists.c: This file contains C functions that handle linked lists for testing 13-is_palindrome.c (provided by Holberton School).
***lists.h: This header file contains definitions and prototypes for all types and functions used in linked_lists.c and 13-insert_number.c.


***14. CPython #0: Python lists

***100-print_python_list_info.c: This C function
***prints basic information about Python lists.

#endif
