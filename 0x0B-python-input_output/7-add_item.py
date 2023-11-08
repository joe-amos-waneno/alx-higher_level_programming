#!/usr/bin/python3
"""Script adding all arguments to a Python list and saving it"""


import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
try:
    py_list = load_from_json_file(file_name)
except FileNotFoundError:
    py_list = []
finally:
    for q in sys.argv[1:]:
        py_list.append(str(q))
    save_to_json_file(py_list, file_name)
