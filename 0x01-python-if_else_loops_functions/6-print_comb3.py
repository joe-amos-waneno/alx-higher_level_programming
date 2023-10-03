#!/usr/bin/python3

for i in range(0, 10):
    for b in range(1, 10):
        if i >= b:
            continue
        if i == 8 and b == 9:
            print("{:d}{:d}".format(i, b))
        else:
            print("{:d}{:d}".format(i, b), end=", ")
