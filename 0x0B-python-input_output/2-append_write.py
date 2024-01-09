#!/usr/bin/python3

"""Funtions that appends a file """

def append_write(filename="", text=""):
    """appends a string at the end """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
