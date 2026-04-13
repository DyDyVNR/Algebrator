""" Custom exception classes for matrix operations """

class MatrixSizeError(Exception):
    """Exception raised for errors in the size of the matrix (not mathematical errors)."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MatrixDimensionError(Exception):
    """Exception raised for errors in matrix dimensions (e.g. non-square matrix for determinant)."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidOptionError(Exception):
    """Exception raised for invalid menu options."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MatrixNotInvertibleError(Exception):
    """Exception raised when attempting to invert a non-invertible matrix."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidInputError(Exception):
    """Exception raised for invalid inputs (e.g. non-numeric values in matrix)."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
