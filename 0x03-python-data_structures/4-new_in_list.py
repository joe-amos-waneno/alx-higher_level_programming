#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    r = [x for x in my_list]
    r[idx] = element
    return (r)
