#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    q = 0
    for l in range(x):
        try:
            print(my_list[l], end="")
            q += 1
        except IndexError:
            break
    print("")
    Return
