#!/usr/bin/python3
"""Creating an object from a json file."""

import json


def load_from_json_file(filename):
    """Creating an object from the json file."""
    with open(filename) as file:
        return json.load(file)
