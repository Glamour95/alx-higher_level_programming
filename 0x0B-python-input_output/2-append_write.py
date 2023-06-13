#!/usr/bin/python3
"""A function that appends a string of a text file"""

def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
