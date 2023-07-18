# alx-higher_level_programming

## Directory: 0x0C-python-almost_a_circle

###Description: The repository is dedicated to the "Almost a Circle" project, which focuses on object-oriented programming in Python. It contains various modules and classes for creating rectangles and squares.

Requirements: Python 3.4 or higher is required to run the scripts in this repository.

File Descriptions: The repository consists of several files, including models/rectangle.py and models/square.py, which define the Rectangle and Square classes, respectively. Other files include test files, a main file, and a base module.

Execution: Instructions are provided on how to execute the Python scripts and test the functionalities of the Rectangle and Square classes. Examples are given for creating instances, printing information, updating attributes, and more.

Task Instructions: The file lists the tasks to be completed as part of the project, including implementing the initialization, area calculation, display, update, and serialization functionalities for rectangles and squares. Each task has its own requirements and example usage.

Conclusion: The README concludes by thanking the user for their attention and encourages them to provide feedback or report any issues they encounter.

### 0. If it's not tested it doesn't work 
All your files, classes, and methods must be unit tested and be PEP 8 validated.

To run the tests, execute the following command in the terminal:
Note: The number of tests you create may differ from the example provided.

### 1. Base class 
Create a class named `Base`:

- Create a folder named `models` with an empty file `__init__.py` inside. This will make the folder a Python package.
- Create a file named `models/base.py`.
- Define the class `Base` with the following specifications:
  - Private class attribute `__nb_objects` set to 0.
  - Class constructor `def __init__(self, id=None)`:
    - If `id` is not `None`, assign the value of `id` to the public instance attribute `id`.
    - If `id` is `None`, increment `__nb_objects` and assign the new value to `id`.
  - The `Base` class will serve as the base for all other classes in this project. Its purpose is to manage the `id` attribute and avoid code duplication.

Example usage:
```python
from models.base import Base

if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

###2. First Rectangle 
Create a class Rectangle that inherits from Base:

Create a file named models/rectangle.py.
Define the class Rectangle with the following specifications:
Inherits from the Base class.
Private instance attributes with corresponding public getter and setter methods:
__width (width)
__height (height)
__x (x)
__y (y)
Class constructor def __init__(self, width, height, x=0, y=0, id=None):
Calls the super class constructor with id.
Assigns the values of width, height, x, and y to the corresponding attributes.
The use of private attributes with getter and setter methods is to protect the attributes and validate the assigned values.
usage:
from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

###3. Validate attributes 
Update the Rectangle class by adding validation to all setter methods and instantiation (excluding id):

If the input is not an integer, raise a TypeError exception with the message: "<name of the attribute> must be an integer". For example: "width must be an integer".
If width or height is less than or equal to 0, raise a ValueError exception with the message: "<name of the attribute> must be >

#endif

