#!/usr/bin/python3
"""Reads and prints a text file (UTF8) to stdout"""

def read_file(filename=""):
    """Reads and prints a text file (UTF8) to stdout"""
    try:
        with open(filename, encoding="utf-8") as f:
            print(f.read(), end="")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
