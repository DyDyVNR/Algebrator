# SLDC: Design Your Tests

## Test Plan

**Manual Testing:**

#### **Test 1: Matrix Addition - Valid Input**

**Goal:** Verify that matrix addition correctly computes the sum of two matrices with matching dimensions.

**Expected Result:** The program will output a matrix where each element is the sum of corresponding elements from the two input matrices.

**Steps:**
1. Run `python main.py`
2. Select option 1 (Addition) from the menu
3. Enter `2 3` when prompted for matrix dimensions (2 rows, 3 columns)
4. For the first matrix, enter the following rows when prompted:
   - Row 1: `1 2 3`
   - Row 2: `4 5 6`
5. For the second matrix, enter the following rows when prompted:
   - Row 1: `7 8 9`
   - Row 2: `10 11 12`
6. Verify the result displays:
```
   [8.0  10.0  12.0]
   [14.0 16.0  18.0]
```

#### **Test 2: Determinant Calculation - 2×2 Matrix**

**Goal:** Calculate the determinant of a 2×2 matrix and verify it matches the hand-calculated result.

**Expected Result:** The program will correctly compute and display the determinant value.

**Steps:**
1. Run `python main.py`
2. Select option 4 (Determinant) from the menu
3. Enter `2 2` for matrix dimensions
4. Enter the following rows:
   - Row 1: `4 7`
   - Row 2: `2 6`
5. Hand-calculate the expected determinant: (4×6) - (7×2) = 24 - 14 = 10 or click on this [link](https://www.wolframalpha.com/input?i=matrix+determinant&assumption=%7B%22F%22%2C+%22Determinant%22%2C+%22detmatrix%22%7D+-%3E%22%7B%7B4%2C+7%7D%2C+%7B2%2C+6%7D%7D%22&assumption=%7B%22C%22%2C+%22matrix+determinant%22%7D+-%3E+%7B%22Calculator%22%2C+%22dflt%22%7D) to check.
6. Verify the program displays `10.0`

#### **Test 3: Determinant Calculation - Non-Square Matrix Error**

**Goal:** Verify that the program handles attempts to calculate determinants of non-square matrices appropriately.

**Expected Result:** The program will raise a `MatrixDimensionError` and display an error message indicating that only square matrices have determinants.

**Steps:**
1. Run `python main.py`
2. Select option 4 (Determinant) from the menu
3. Enter `2 3` for matrix dimensions (non-square)
4. Enter elements for the matrix (any valid numbers)
5. Verify an error message appears stating `Only square matrices have determinants`
6. Verify the program does not crash and asks the user if they want to try again and return to the menu.

#### **Test 4: Matrix Inversion - Zero-determinant Matrix Error**

**Goal:** Verify that the program correctly identifies and handles non-invertible (singular) matrices.

**Expected Result:** The program will raise a `MatrixNotInvertibleError` and display an error message indicating that the matrix is singular (determinant = 0) and cannot be inverted.

**Steps:**
1. Run `python main.py`
2. Select option 6 (Matrix Inversion) from the menu
3. Enter `2 2` for matrix dimensions
4. Enter the following rows (this matrix has determinant = 0):
   - Row 1: `1 2`
   - Row 2: `2 4`
5. Verify an error message appears stating the matrix is not invertible because the determinant is 0.
6. Verify the program does not crash and asks the user if they want to try again and return to the menu.


* Edge Cases and Error Handling - Test empty matrices, single-element matrices, and extremely large matrices. Verify that all exception classes work properly and provide meaningful error messages.

#### **Test 5: Edge Case - 1×1 Matrix Operations**

**Goal:** Verify that the program correctly handles the smallest valid matrix size (1×1) for various operations.

**Expected Result:** The program will successfully perform operations on 1×1 matrices and produce correct results.

**Steps:**
1. Run `python main.py`
2. Select option 4 (Determinant)
3. Enter `1 1` for matrix dimensions
4. Enter a single value: `5`
5. Verify the determinant is displayed as `5.0`
6. Enter `y` and return to the menu
7. Select option 6 (Matrix Inversion)
8. Enter `1 1` for matrix dimensions
9. Enter a single value: `5`
10. Verify the inverse is displayed as `[0.2]` (since 1/5 = 0.2)



**Automated Testing:**
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

*Open the terminal and run `pytest`. If pytest is not installed, run `pip install pytest`. See [test_matrix.py](../test_matrix.py) for more detailed individual tests.*


## Video Demonstration of Your Testing

Click on this [link](https://youtu.be/ztae-P4yQS4) for the demonstration video.