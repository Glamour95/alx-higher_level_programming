#!/usr/bin/python3
"""Defines a file-writing function and returns the characters"""

def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
