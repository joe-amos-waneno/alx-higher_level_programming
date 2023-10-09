#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for q in matrix:
        for m in q:
            print("{:d}".format(m), end=" " if m != q[-1] else "")
        print()
