#!/usr/bin/python3
"""Saves the json representation of the object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """Save json representation of my_obj to a specified file."""
    with open(filename, 'w') as file:
        return file.write(json.dumps(my_obj))
