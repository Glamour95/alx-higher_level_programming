#!/usr/bin/python3
"""Creates an Object from a “JSON file”"""

import json

def load_from_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
