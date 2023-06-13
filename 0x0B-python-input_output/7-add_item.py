import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

if path.isfile(filename):
    # Load existing data from file
    my_list = load_from_json_file(filename)
else:
    # Create a new empty list
    my_list = []

# Add the command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
