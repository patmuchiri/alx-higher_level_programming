#!/usr/bin/python3
def append_write(filename="", text=""):
    """defines a function that appends a string and
    returns the number of characters added."""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
