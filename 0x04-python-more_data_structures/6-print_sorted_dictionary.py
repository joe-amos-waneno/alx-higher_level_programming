#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered = list(a_dictionary.keys())
    ordered.sort()
    for q in ordered:
        print("{}: {}".format(q, a_dictionary.get(q)))
