###0x06-python-classes###

0. My first square
File: 0-square.py
Write an empty class Square that defines a square.

You are not allowed to import any module.

Usage:

Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

Output: 

<class '0-square.Square'>
{}

1. Square with size
File: 1-square.py
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
Why is size a private attribute?

The size of a square is crucial for a square, as many things depend on it (e.g., area computation). So, as a class builder, you must control the type and value of this attribute. One way to have control is to keep it private. You will see in the next tasks how to get, update, and validate the size value.

Usage:

Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

Output:

<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'

2. Size validation
File: 2-square.py
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
You are not allowed to import any module

Usage:

Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

Output:

<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0

3. Area of a square
File: 3-square.py
Write a class Square that defines a square by:

Private instance attribute:

class Square:
    def __init__(self, size):
        self.__size = size

In this code, we define the Square class with a constructor method __init__. The constructor takes a parameter size, which represents the size of the square. The attribute __size is prefixed with double underscores, which indicates that it's a private attribute. This convention helps to indicate that the attribute should not be accessed or modified directly from outside the class.

#endif 
