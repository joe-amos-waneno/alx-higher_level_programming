#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    d = 0

    for q in my_list:
        number += q[0] * q[1]
        d += q[1]

    return (number / d)
