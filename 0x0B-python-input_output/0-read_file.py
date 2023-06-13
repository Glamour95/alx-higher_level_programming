#!/usr/bin/python3
"""Reads and prints a text file (UTF8) to stdout"""

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.read()
        print(contents)
