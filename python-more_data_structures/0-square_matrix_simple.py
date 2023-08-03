#!usr/bin/env/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = [[num**2 for num in row] for row in matrix]
    return result_matrix

