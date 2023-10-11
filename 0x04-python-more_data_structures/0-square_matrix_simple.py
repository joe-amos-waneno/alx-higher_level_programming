#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_m = matrix.copy()

    for q in range(len(matrix)):
        n_m[q] = list(map(lambda x: x**2, matrix[q]))

    return (n_m)
