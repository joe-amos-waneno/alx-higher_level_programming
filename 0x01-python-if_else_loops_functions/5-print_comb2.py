#!/usr/bin/python3
for numx in range(0, 100):
    if numx == 99:
        print("{0:02d}".format(numx))
    else:
        print("{0:02d},".format(numx), end=" ")
