#!/usr/bin/python3
"""returns an object representation of a json string"""

import json


def from_json_string(my_str):
    """return an object representation of the string my_str."""
    return json.loads(my_str)
