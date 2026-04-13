from matrix import Matrix
import exception as e

def test_set_matrix_data():
    """ Test setting matrix data """
    matrix = Matrix(2, 2)
    data = [
        [1, 2],
        [3, 4]
    ]
    matrix.set_data(data)
    assert matrix.get_data() == data, "Matrix data was not set correctly"

def test_matrix_addition():
    """ Test matrix addition operation for 2x3 matrices """
    matrix_A = Matrix(2, 3)
    matrix_B = Matrix(2, 3)

    matrix_A.set_data([
        [1, 2, 3],
        [4, 5, 6]
    ])
    matrix_B.set_data([
        [7, 8, 9],
        [10, 11, 12]
    ])
    result = matrix_A + matrix_B
    assert result.get_data() == [
        [8.0, 10.0, 12.0],
        [14.0, 16.0, 18.0]
    ], "Matrix addition result is incorrect"

def test_matrix_subtraction():
    """ Test matrix subtraction operation for 2x2 matrices """
    matrix_A = Matrix(2, 2)
    matrix_B = Matrix(2, 2)

    matrix_A.set_data([
        [5, 6],
        [7, 8]
    ])
    matrix_B.set_data([
        [1, 2],
        [3, 4]
    ])
    result = matrix_A - matrix_B
    assert result.get_data() == [
        [4.0, 4.0],
        [4.0, 4.0]
    ], "Matrix subtraction result is incorrect"

def test_matrix_multiplication():
    """ Test matrix multiplication operation for 9x9 and 9x2 matrices """
    matrix_A = Matrix(9, 9)
    matrix_B = Matrix(9, 2)

    matrix_A.set_data([
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ])
    matrix_B.set_data([
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10],
        [11, 12],
        [13, 14],
        [15, 16],
        [17, 18]
    ])
    result = matrix_A * matrix_B
    assert result.get_data() == [
      [525.0, 570.0],
      [525.0, 570.0],
      [525.0, 570.0],
      [525.0, 570.0],
      [525.0, 570.0],
      [525.0, 570.0],
      [525.0, 570.0],
      [525.0, 570.0],
      [525.0, 570.0]
    ], "Matrix multiplication result is incorrect"
    # reference result: https://www.wolframalpha.com/input?i2d=true&i=matrix+multiplication&assumption=%7B%22F%22%2C+%22MatricesOperations%22%2C+%22theMatrix2%22%7D+-%3E%22%7B%7B1%2C+2%7D%2C+%7B3%2C+4%7D%2C%7B5%2C6%7D%2C%7B7%2C8%7D%2C%7B9%2C10%7D%2C%7B11%2C12%7D%2C%7B13%2C14%7D%2C%7B15%2C16%7D%2C%7B17%2C18%7D%7D%22&assumption=%7B%22F%22%2C+%22MatricesOperations%22%2C+%22theMatrix1%22%7D+-%3E%22%7B%7B1%2C2%2C3%2C+4%2C5%2C6%2C7%2C8%2C9%7D%2C+%7B1%2C2%2C3%2C+4%2C5%2C6%2C7%2C8%2C9%7D%2C+%7B1%2C2%2C3%2C+4%2C5%2C6%2C7%2C8%2C9%7D%2C+%7B1%2C2%2C3%2C+4%2C5%2C6%2C7%2C8%2C9%7D%2C+%7B1%2C2%2C3%2C+4%2C5%2C6%2C7%2C8%2C9%7D%2C+%7B1%2C2%2C3%2C+4%2C5%2C6%2C7%2C8%2C9%7D%2C+%7B1%2C2%2C3%2C+4%2C5%2C6%2C7%2C8%2C9%7D%2C+%7B1%2C2%2C3%2C+4%2C5%2C6%2C7%2C8%2C9%7D%2C+%7B1%2C2%2C3%2C+4%2C5%2C6%2C7%2C8%2C9%7D%7D%22&assumption=%7B%22C%22%2C+%22matrix+multiplication%22%7D+-%3E+%7B%22Calculator%22%2C+%22dflt%22%7D

def test_matrix_multiplication_error():
    """ Test that matrix multiplication raises error for incompatible dimensions """
    matrix_A = Matrix(2, 3)
    matrix_B = Matrix(4, 2)

    matrix_A.set_data([
        [1, 2, 3],
        [4, 5, 6]
    ])
    matrix_B.set_data([
        [7, 8],
        [9, 10],
        [11, 12],
        [13, 14]
    ])
    try:
        result = matrix_A * matrix_B
        assert False, "MatrixDimensionError was not raised for incompatible dimensions"
    except e.MatrixDimensionError:
        pass  # Expected
    
def test_matrix_transpose():
    """ Test matrix transposition """
    matrix = Matrix(2, 3)
    matrix.set_data([
        [1, 2, 3],
        [4, 5, 6]
    ])
    transposed = matrix.transpose()
    assert transposed.get_data() == [
        [1, 4],
        [2, 5],
        [3, 6]
    ], "Matrix transposition result is incorrect"

def test_matrix_determinant():
    """ Test matrix determinant calculation """
    matrix = Matrix(3, 3)
    matrix.set_data([
        [6, 1, 1],
        [4, -2, 5],
        [2, 8, 7]
    ])
    det = matrix.determinant()
    assert det == -306, "Matrix determinant result is incorrect"
    # reference result: https://www.wolframalpha.com/input?i=determinant+%7B%7B6%2C1%2C1%7D%2C+%7B4%2C-2%2C5%7D%2C+%7B2%2C8%2C7%7D%7D

def test_matrix_determinant_error():
    """ Test that determinant raises error for non-square matrix """
    matrix = Matrix(2, 3)
    matrix.set_data([
        [1, 2, 3],
        [4, 5, 6]
    ])
    try:
        det = matrix.determinant()
        assert False, "MatrixDimensionError was not raised for non-square matrix"
    except e.MatrixDimensionError:
        pass  # Expected

def test_matrix_inverse():
    """ Test matrix inversion """
    matrix = Matrix(2, 2)
    matrix.set_data([
        [4, 7],
        [2, 6]
    ])
    inverse = matrix.inverse()
    assert inverse.get_data() == [
        [0.6, -0.7],
        [-0.2, 0.4]
    ], "Matrix inversion result is incorrect"
    # reference result: https://www.wolframalpha.com/input?i=inverse+%7B%7B4%2C7%7D%2C+%7B2%2C6%7D%7D

def test_matrix_inverse_error():
    """ Test that inverse raises error for non-invertible matrix"""
    matrix = Matrix(2, 2)
    # determinant is zero
    matrix.set_data([
        [1, 2],
        [2, 4]
    ])
    try:
        inv = matrix.inverse()
        assert False, "MatrixNotInvertibleError was not raised for non-invertible matrix"
    except e.MatrixNotInvertibleError:
        pass  

    # non-square matrix
    matrix = Matrix(2, 3)
    matrix.set_data([
        [1, 2, 3],
        [4, 5, 6]
    ])
    try:
        inv = matrix.inverse()
        assert False, "MatrixDimensionError was not raised for non-square matrix"
    except e.MatrixDimensionError:
        pass

def test_matrix_row_reduce_echelon():
    """ Test matrix row reduction to echelon form """
    matrix = Matrix(3, 3)
    matrix.set_data([
        [1, 2, -1],
        [2, 4, -2],
        [-1, -2, 1]
    ])
    rref_matrices, desc = list(matrix.row_reduce_echelon())[-1] # Get the final matrix after all steps
    assert rref_matrices.get_data() == [
        [1.0, 2.0, -1.0],
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0]
    ], "Matrix row reduction to echelon form is incorrect"
    # reference result: https://www.wolframalpha.com/input?i=row+reduction+calculator&assumption=%7B%22F%22%2C+%22ReducedRowEchelon%22%2C+%22theMatrix%22%7D+-%3E%22%7B%7B1%2C+2%2C+-1%7D%2C+%7B2%2C+4%2C+-2%7D%2C+%7B-1%2C+-2%2C+1%7D%7D%22