#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = matrix.copy()
    for i in range(len(matrix)):
        squared[i]  = list(map(lambda x: x*x, matrix[i]))
    return (squared)
