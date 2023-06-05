Rectangle Class

This project contains a Python class called Rectangle that represents a rectangle. The class provides methods and attributes to manipulate and retrieve information about rectangles.

0. Simple Rectangle
The Rectangle class is defined in the file 0-rectangle.py. It is an empty class with no methods or attributes.

1. Real definition of a rectangle
The Rectangle class is defined in the file 1-rectangle.py. It has the following features:

Private instance attributes: width and height
Getters and setters for width and height
Instantiation with optional width and height parameters
2. Area and Perimeter
The Rectangle class is defined in the file 2-rectangle.py. It extends the previous version with additional features:

Public instance methods: area() and perimeter() to calculate the area and perimeter of the rectangle
Validation checks for the width and height attributes
3. String Representation
The Rectangle class is defined in the file 3-rectangle.py. It extends the previous version with additional features:

The __str__() and __repr__() methods are implemented to provide string representations of the rectangle
The rectangle is represented using the character '#'
If the width or height is 0, an empty string is returned
4. Eval is Magic
The Rectangle class is defined in the file 4-rectangle.py. It extends the previous version with additional features:

The __repr__() method is updated to return a string representation of the rectangle that can be used to recreate a new instance using eval()
5. Detect Instance Deletion
The Rectangle class is defined in the file 5-rectangle.py. It extends the previous version with additional features:

A message "Bye rectangle..." is printed when an instance of Rectangle is deleted
6. How Many Instances
The Rectangle class is defined in the file 6-rectangle.py. It extends the previous version with additional features:

A class attribute number_of_instances is added to keep track of the number of instances of Rectangle
The attribute is incremented during each new instance creation and decremented during instance deletion
7. Change Representation
The Rectangle class is defined in the file 7-rectangle.py. It extends the previous version with additional features:

The string representation of the rectangle is changed to use the symbol '@' instead of '#'
Please refer to the individual files in the project repository for the complete implementation of each version of the Rectangle class.

Author
This project is implemented by Glamour Maphanga.
