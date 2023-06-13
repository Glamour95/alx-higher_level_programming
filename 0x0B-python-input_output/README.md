###0x0B-python-input_output
0. Read file
This program contains a function called read_file that reads a text file (UTF8) and prints its contents to stdout.

Function Signature

def read_file(filename="")

Parameters
filename (str): The name of the file to be read. Defaults to an empty string.
Output
The function prints the contents of the file to stdout.

Usage

read_file("my_file_0.txt")

1. Write to a file
This program contains a function called write_file that writes a string to a text file (UTF8) and returns the number of characters written.

Function Signature

def write_file(filename="", text="")

Parameters
filename (str): The name of the file to be written. Defaults to an empty string.
text (str): The string to be written to the file. Defaults to an empty string.
Output
The function returns the number of characters written to the file.

Usage

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

2. Append to a file
This program contains a function called append_write that appends a string at the end of a text file (UTF8) and returns the number of characters added.

Function Signature

def append_write(filename="", text="")

Parameters
filename (str): The name of the file to which the string should be appended. Defaults to an empty string.
text (str): The string to be appended to the file. Defaults to an empty string.
Output
The function returns the number of characters added to the file.

Usage

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

3. To JSON string
This program contains a function called to_json_string that takes an object (string) and returns its JSON representation.

Function Signature

def to_json_string(my_obj)

Parameters
my_obj (obj): The object (string) to be converted to JSON.
Output
The function returns a JSON string representation of the object.

Usage

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)

4. From JSON string to Object
This program contains a function called from_json_string that takes a JSON string and returns the corresponding object (Python data structure).

Function Signature

def from_json_string(my_str)

Parameters
my_str (str): The JSON string to be converted to an object.
Output
The function returns the object represented by the JSON string.

Usage

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)

# Input/Output in Python

This repository contains Python scripts that demonstrate input/output operations in Python.

## 5. Save Object to a file

### Description

This script defines a function `save_to_json_file(my_obj, filename)` that writes an object to a text file using a JSON representation. The function uses the `json` module to serialize the object and write it to the file. The function accepts two parameters: `my_obj`, the object to be saved, and `filename`, the name of the file.

The script also provides an example usage of the `save_to_json_file` function.

```python
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = {
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = {132, 3}
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

6. Create object from a JSON file
Description
This script defines a function load_from_json_file(filename) that creates an object from a JSON file. The function uses the json module to deserialize the JSON data from the file and create the corresponding object. The function accepts one parameter: filename, the name of the JSON file.

The script also provides an example usage of the load_from_json_file function.

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

7. Load, add, save
Description
This script demonstrates how to add items to a Python list and save them to a file. The script uses the save_to_json_file function from the previous script to save the list as a JSON representation in a file named add_item.json. If the file doesn't exist, it will be created.

The script provides an example usage of the script.

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_item_to_list():
    try:
        filename = "add_item.json"
        items = []
        
        # Load existing items from file
        if os.path.exists(filename):
            items = load_from_json_file(filename)
        
        # Add new items from command line arguments

##endif
