#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tms = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            tms.append(True)
        else:
            tms.append(False)
    return (tms)
