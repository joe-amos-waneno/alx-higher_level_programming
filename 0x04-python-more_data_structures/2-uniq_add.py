#!/usr/bin/python3
def uniq_add(my_list=[]):
    myList = set(my_list)
    integer = 0

    for i in myList:
        integer += i

    return (integer)
