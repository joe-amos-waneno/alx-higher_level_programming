#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numOfElements = 0

    for q in range(0, x):
        try:
            print("{:d}".format(my_list[q]), end="")
            numOfElements += 1
        except (TypeError, ValueError):
            continue
    print()
    return numOfElements
