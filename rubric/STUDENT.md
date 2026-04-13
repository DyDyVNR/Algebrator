# CIT 128 Project: Student Directed Project Student Rubric

**Version:** 5/27/2024

The student provided rubric below is worth **50 points** and is specific to the individual student directed project description. Students may decide how to divide up the points in consultation with the instructor who will complete a Pull Request with changes that you must successfully merge into your code. The instructor may choose to modify the rubric or points distribution at any time and will [approve the final rubric](../assignment/APPROVALS.md). Once approved, you may not modify this file without putting in a change request with the instructor.

If no modifications are made to the Student Grading Rubric or the rubric was not approved in the provided section the instructor, no points will be awarded from this section. Students may **not** use any element listed in the instructor rubric as part of the student rubric. If you are having trouble where to start, look at the [TIPS.md](../assignment/TIPS.md) file for ideas.

---

## Student Grading Rubric (50pt)

### Accuracy and Correctness of Calculation (25pt)
* All matrix operations perform and yield correct results (16pt)
    - RREF produces correct reduced row echelon form (4pt)
    - Determinant calculations are accurate (4pt)
    - Matrix inversion works correctly for invertible matrices (4pt)
    - All operations such as addition, subtraction, multiplication, inverse, transpose, determinant, and rref handle matrices from 1×1 up to 10×10 (4pt)

* Edge cases and special matrices are handled correctly (9pt)
    - 1x1 and non-invertible matrices return appropriate result or error (3pt)
    - Identity, zero, and 0-determinant matrices (3pt)
    - Matrices with zero rows or columns (3pt)

### Unit Testing (15pt)
* Passes every unit test(10pt)
    - All test cases pass without errors, including:
        - **Matrix data management** (`test_set_matrix_data`): Matrices properly store and retrieve data
        - **Matrix addition** (`test_matrix_addition`): Correct results for matrices of matching dimensions
        - **Matrix subtraction** (`test_matrix_subtraction`): Correct results for matrices of matching dimensions
        - **Matrix multiplication** (`test_matrix_multiplication`): Correct results for compatible matrix dimensions (including larger matrices)
        - **Matrix multiplication error handling** (`test_matrix_multiplication_error`): Raises `MatrixDimensionError` for incompatible dimensions
        - **Matrix transposition** (`test_matrix_transpose`): Correct transformation of rows to columns
        - **Determinant calculation** (`test_matrix_determinant`): Accurate determinant for square matrices
        - **Determinant error handling** (`test_matrix_determinant_error`): Raises `MatrixDimensionError` for non-square matrices
        - **Matrix inversion** (`test_matrix_inverse`): Correct inverse for invertible square matrices
        - **Inversion error handling** (`test_matrix_inverse_error`): Raises `MatrixNotInvertibleError` for singular matrices and `MatrixDimensionError` for non-square matrices
        - **Row reduce enchelon** (`test_matrix_row_reduce_echelon`): Correctly yields rref for a matrix
    - Tests run successfully without modification to test file

* Test quality (5pt)
    - Unit tests cover an appropriate amount of test cases (2pt)
    - Tests are well-organized with descriptive names (2pt)
    - Proper use of assertions and test structure (1pt)

### User Prompt and Interface (10pt)
* Proper user inputs and error handling (5pt)
    - Clear prompts for each input step (1pt)
    - Invalid matrix dimensions/formats are caught and reported (1pt)
    - Invalid menu options handled appropriately (1pt)
    - Non-numeric inputs validated appropriately (1pt)
    - Helpful messages for mathematical errors, for example when trying to find the determinant of a non-sqaure matrix (1pt)

* Clear menus and instructions (5pt)
    - Main menu clearly lists all available operations (2pt)
    - Matrix input format is explained to user (1pt)
    - Results are displayed in readable format (1pt)
    - Step-by-step RREF operations are clearly formatted (1pt)

