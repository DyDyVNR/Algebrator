import exception as e

class Matrix:
    """
        This class represents a matrix of size m by n. The maximum size is 10 x 10.
        Arg:
            num_row: Number of rows (int)
            num_col: Number of cols (int)
        
        Attributes:
            data: 2D list representing the matrix data
    """
    def __init__(self, num_row, num_col):
        """ Initialize a matrix of size m by n with all values set to 0 """
        if num_row > 10 or num_col > 10:
            raise e.MatrixSizeError("Matrix size cannot be over 10 x 10!")
        if num_row <= 0 or num_col <= 0:
            raise e.MatrixSizeError("Matrix dimensions must be positive integers!")
        
        self.data = [[0 for _ in range(num_col)] for _ in range(num_row)]

    def set_data(self, data):
        """ Set the matrix data """
        self.data = data

    def get_data(self):
        """ Get the matrix data """
        return self.data
        
    def __add__(self, other):
        """ Add two matrices """
        if type(other) != Matrix:
            raise TypeError("Operand must be a matrix")
        
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise e.MatrixDimensionError("Matrices must have the same dimensions to be added")
        
        result = Matrix(len(self.data), len(self.data[0]))
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result
    
    def __sub__(self, other):
        """ Subtract two matrices """
        if type(other) != Matrix:
            raise TypeError("Operand must be a matrix")
        
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise e.MatrixDimensionError("Matrices must have the same dimensions to be subtracted")
        
        result = Matrix(len(self.data), len(self.data[0]))
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result
    
    def __mul__(self, other):
        """ Multiply two matrices """
        if type(other) != Matrix:
            raise TypeError("Operand must be a matrix")
        
        if len(self.data[0]) != len(other.data):
            raise e.MatrixDimensionError("Number of columns in the first matrix must equal number of rows in the second matrix")
        
        result = Matrix(len(self.data), len(other.data[0]))
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def __repr__(self):
        """ Display format of a matrix """

        tolerance = 10 ** -7 #tolerance for floating-point comparisons to avoid precision issues
        display_matrix = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[i])):
                # Clean up the value
                val = self.data[i][j]
                if abs(val) < tolerance: # Treat very small values as zero
                    val = 0.0
                else:
                    val = round(val, 4)  # Round to 4 decimal places for display

                row.append(str(f"{val:>10}")) #right align each element within 10 spaces to improve readability
            display_matrix.append(" ".join(row))
        return "\n".join(display_matrix)

    def transpose(self):
        """ Transpose the matrix """
        transposed = Matrix(len(self.data[0]), len(self.data)) #switch dimensions
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                transposed.data[j][i] = self.data[i][j]
        return transposed
    
    def inverse(self):
        """ Inverse a square matrix """
        if len(self.data) != len(self.data[0]):
            raise e.MatrixDimensionError("Only square matrices can be inverted")
        
        if self.determinant() == 0:
            raise e.MatrixNotInvertibleError("Matrix is not invertible (determinant is 0)")
        
        # For 1x1 matrix, the inverse is 1/value
        if len(self.data) == 1:
            inverted = Matrix(1, 1)
            inverted.data[0][0] = 1 / self.data[0][0]
            return inverted
        
        # For 2x2 matrix, use the formula
        if len(self.data) == 2:
            det = self.determinant()
            inverted = Matrix(2, 2)
            inverted.data[0][0] = self.data[1][1] / det
            inverted.data[0][1] = -self.data[0][1] / det
            inverted.data[1][0] = -self.data[1][0] / det
            inverted.data[1][1] = self.data[0][0] / det
            return inverted
        
        # For larger matrices, use the adjoint method
        size = len(self.data)
        adjoint = Matrix(size, size)
        for i in range(size):
            for j in range(size):
                # Create minor matrix
                minor = [] #exclude i-th row and j-th column to form minor
                for k, row in enumerate(self.data):
                    if k != i: #skip i-th row
                        minor_row = row[:j] + row[j+1:] #skip j-th column
                        minor.append(minor_row)
                minor_matrix = Matrix(size - 1, size - 1)
                minor_matrix.set_data(minor)
                cofactor = ((-1) ** (i + j)) * minor_matrix.determinant() #calculate cofactor based on the formula -1^(i+j) * det(minor)
                adjoint.data[j][i] = cofactor 

        # Multiply adjoint by 1/det to get inverse
        det = self.determinant()
        for i in range(size):
            for j in range(size):
                adjoint.data[i][j] /= det
        return adjoint

    def determinant(self):
        """ Calculate the determinant of a square matrix """
        if len(self.data) != len(self.data[0]):
            raise e.MatrixDimensionError("Only square matrices have determinants")
        
        # base cases for 1x1 and 2x2 matrices
        if len(self.data) == 1:
            return self.data[0][0]
        if len(self.data) == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        
        # recursion for 3x3 matrices or larger
        det = 0
        for c in range(len(self.data)):
            minor = [row[:c] + row[c+1:] for row in self.data[1:]] 
            new_matrix = Matrix(len(minor), len(minor))
            new_matrix.set_data(minor)
            det += ((-1) ** c) * self.data[0][c] * new_matrix.determinant() 
        return det

    def row_reduce_echelon(self):
        """ Row-reduce a matrix to echelon form 
            Yields each step of the row-reduction process as a tuple (matrix, description)
            Returns the final row-reduced matrix
         """

        num_rows = len(self.data)
        num_cols = len(self.data[0])

        matrix = Matrix(num_rows, num_cols) #create a copy of the original matrix
        matrix.set_data([row[:] for row in self.data])
        
        yield (matrix, "Initial matrix:") #yield initial matrix state
        
        pivot_row = 0
        tolerance = 10 ** -7 #tolerance for floating-point comparisons to avoid precision issues
        
        for col in range(num_cols):
            if pivot_row >= num_rows:
                break
            
            # Find pivot
            max_row = pivot_row
            for row in range(pivot_row + 1, num_rows):
                if abs(matrix.data[row][col]) > abs(matrix.data[max_row][col]):
                    max_row = row
            
            # Skip if essentially zero
            if abs(matrix.data[max_row][col]) < tolerance:
                continue
            
            # Swap 2 rows
            if max_row != pivot_row:
                matrix.data[pivot_row], matrix.data[max_row] = matrix.data[max_row], matrix.data[pivot_row]
                yield (matrix, f"Swap R{pivot_row + 1} <-> R{max_row + 1}") #yield after row swap
            
            # Scale pivot row
            pivot_value = matrix.data[pivot_row][col]
            if abs(pivot_value - 1.0) > tolerance:
                for j in range(num_cols):
                    matrix.data[pivot_row][j] /= pivot_value
                yield (matrix, f"R{pivot_row + 1} / {pivot_value:.2f} -> R{pivot_row + 1}") #yield after scaling pivot row
            
            # Eliminate other entries
            for row in range(num_rows):
                if row != pivot_row and abs(matrix.data[row][col]) > tolerance:
                    factor = matrix.data[row][col]
                    for j in range(num_cols):
                        matrix.data[row][j] -= factor * matrix.data[pivot_row][j]
                    yield (matrix, f"R{row + 1} - ({factor:.2f})R{pivot_row + 1} -> R{row + 1}") #yield after eliminating other rows
            
            pivot_row += 1
        
        # Return final matrix
        result = Matrix(num_rows, num_cols)
        result.set_data(matrix.data)
        return result

