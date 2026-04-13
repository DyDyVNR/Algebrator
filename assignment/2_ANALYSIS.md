# SLDC: Analyze Your Project

## Analysis

### Functional Requirements

* The program must perform linear operations, including addition, subtraction, multiplication, transposition, inverse, and row-reduce enchelon.
* The program must accept a single or multiple matrices from users as input.
* The program must output the solutions based on selected operations by the user and accurately display the result.
* For certain operations, like the row-reduce echelon, the program must show steps for each calculation so that users can understand the process rather than just receiving an answer.

### Non-Functional Requirements

* Performance: The system must make sure that the computation does not take too long to return the solution. All supported operations should complete in about 2 to 3 seconds or less.
* Constaint: To ensure efficiency, some limitations will be introduced; for example, the maximum matrix size is capped at 10x10.
* Usability: The interface must be intuitive with clear errors or warnings if users input the wrong format. It should prompt the users on what to input with clear instructions.
* Scalability: This system should be designed for future expansion by adding more features and operations.
* Reliability: The program must have 99.9% uptime since it's running locally. Also, if an error occurs during computation, the program must handle the errors and appropriately provide feedback to the users.

---

## Student Selected SDLC Analysis Concepts

### Use Case

**Actor**: A student who needs to find the inverse of a matrix for solving systems of equations, transformations, or other linear algebra applications.
**Goal**: To obtain the inverse of a square matrix.

**System Process**:

Normal Flow:
* Student selects option 6 "Matrix Inversion" from the main menu
* System prompts: "Please enter number of rows and columns separated by space: "
* Student enters matrix size (e.g., "3, 3")
* System validates input is a positive integer between 1 and 10
* System prompts: "Please enter the matrix data row by row, with each element separated by space: "
* Student enters elements for each row sequentially
* System validates all inputs (correct count, numeric values)
* System calculates the determinant and check if it is a square matrix to verify if it's invertible
* System performs the matric inversion algorithm
* System displays: "Inverse Matrix:" followed by the calculated inverse matrix
* System asks the user if they would like to perform another calculation and returns to main menu or exit.

Alternative Scenarios:
* Invalid matrix size: If student enters invalid size, system displays "Error: Please enter an integer between 1 and 10" and returns to step 2
* Input validation errors: Same handling as previous use cases for element count and numeric validation
* Matrix with determinant = 0: System displays "Error: Matrix is not invertible (determinant is 0)".

### Technical Requirements:

**Development Environment**
* Programming language: Python, easy to maintain and excellent for mathematical computations
* Required library: pyfiglet - library for fomatting text fonts to display on terminal
* Testing framework: pytest
* Development tools: Visual Studio Code, Version Control Git
**Performance Requiurements**
* Computational performance: Each operational computation must take less than 0.5 seconds to complete
* Algorithm time complexity: $O(n^{3})$ for multiplication, inverse, determinant, and rref.
* Space complexity: $O(n \times m)$ to store a matrix
* Constraint: maximum matrix dimension 10 x 10
**Security and Error Handling**
* Validate all user inputs before processing
* Clear, user-friendly error messages
* Error types: validation errors (invalid dimension input, non-numeric input) and mathematical errors (dimension mismatch)
**Testing**
* Unit test for individual operations/methods
* Edge case testing


### Reference
* [Dias, Erica. “The Ultimate Guide to Technical Requirements for 2024.” ClickUp, 12 Jan. 2024,](https://clickup.com/blog/technical-requirements/)