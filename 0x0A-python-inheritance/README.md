Python inheritence

This repository contains Python scripts for solving various tasks related to inheritance in Python.

Task 0: Lookup
In this task, the goal is to write a function lookup(obj) that returns the list of available attributes and methods of an object. The function takes an object as a parameter and returns a list object. The function does not import any module.

Usage:

lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

Output:

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

Task 1: My list
In this task, the goal is to write a class MyList that inherits from the list class. The MyList class has a public instance method print_sorted(self) that prints the list, but sorted in ascending order. It is assumed that all elements of the list are of type int. The class does not import any module.

Usage:

MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

Output:

[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]

2. Exact same object

Write a function is_same_class(obj, a_class) that returns True if the object obj is exactly an instance of the specified class a_class, and False otherwise.
def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    return False
3. Same class or inherit from

Write a function is_kind_of_class(obj, a_class) that returns True if the object obj is an instance of a_class or if it is an instance of a class that inherited from a_class. Otherwise, it should return False.

def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False

5. Geometry module

Create an empty class BaseGeometry without any attributes or methods.

class BaseGeometry:
    pass

6. Improve Geometry

Improve the BaseGeometry class by adding a public instance method area(self) that raises an exception with the message "area() is not implemented".

class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
7. Integer validator

Add a public instance method integer_validator(self, name, value) to the BaseGeometry class. This method should validate that value is an integer:

If value is not an integer, it should raise a TypeError exception with the message "<name> must be an integer".
If value is less than or equal to 0, it should raise a ValueError exception with the message "<name> must be greater than 0".

class BaseGeometry:
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
8. Rectangle

Create a class Rectangle that inherits from BaseGeometry. The Rectangle class should have a constructor __init__(self, width, height):

The width and height must be private attributes.
The width and height must be validated by using the integer_validator method from the BaseGeometry class.

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
9. Full rectangle

In the Rectangle class, override the __str__ method to return a string representation of the rectangle in the format [Rectangle] <width>/<height>.
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

   

