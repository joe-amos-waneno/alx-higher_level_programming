#!/usr/bin/python3

def pow(a, b):
    rs = 1
    ba = 1
    n = 0
    if b < 0:
        n = b
        b = (-1) * b

    for i in range(b):
        rs *= a
        ba = rs * rs

    if n < 0:
        rs /= ba
    return rs
