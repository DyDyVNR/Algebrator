# SDLC: Deploy Your Project

## Install Instructions

**Before running the program, make sure pyfiglet library is installed and Git is installed on your machine.**

* To check if Git is installed, open the Command Prompt (on window) or Terminal (on Mac), and type `git --version`.

* To install pyfiglet, open the terminal, and execute the following command: `pip install pyfiglet`. To check if pyfiglet has been installed, run the following command `pyfiglet --version`. 

## Execute the Software

* Navigate to the project repository on Github using the following [link](https://github.com/RHC-CIT-128-FA25/starter-project-cs-DyDyVNR.git).

* Clone the project from Github to the local repository. To clone the project, do the following:
    - Create a folder on the local machine.
    - Open the folder via visual studio code or the terminal.
    - Open up the terminal and go to the folder directory that has just been created by using `cd` command.
    - Execute following command `git clone https://github.com/RHC-CIT-128-FA25/starter-project-cs-DyDyVNR`.
* Go to the project directory called `starter-project-cs-DyDyVNR` and run the `main.py` file to start the program.

## Use the Software

* After executing `main.py`, the program will display the welcome message along with an array of menu options.
* Select one of the options to perform a matrix operation:

### **Addition & Subtraction**
* Select option 1 for addition or option 2 for subtraction.
* Enter the number of rows and columns separated by a space only (e.g. for a 2x3 matrix, enter `2 3`).
* The program will prompt one row at a time; enter each number separated by a space.
* Repeat the same process for the second matrix.
* The result will be displayed in the matrix format.

### **Multiplication**
* Select option 3 for multiplication.
* Enter the number of rows and columns of the first matrix separated by a space only (e.g. for a 2x3 matrix, enter `2 3`).
* The program will prompt one row at a time; enter each number separated by a space.
* Repeat the same process for the second matrix. **Note** The number of columns in the first matrix must equal the number of rows in the second matrix.
* The result will be displayed in matrix format.

### **Calculate Determinant**
* Select option 4 to calculate the determinant of a matrix.
* Enter the number of rows and columns of the first matrix separated by a space only. Keep in mind that only square matrices (nxn) have determinants.
* The program will prompt one row at a time; enter each number separated by a space.
* The determinant will be displayed as a decimal value.

### **Transpose**
* Select option 5 to transpose a matrix.
* Enter the number of rows and columns of the first matrix separated by a space only (e.g. for 2x3 matrices, enter `2 3`).
* The program will prompt one row at a time; enter each number separated by a space.
* The transposed matrix will be displayed in matrix format.

### **Inverse**
* Select option 6 to find the inverse of a matrix.
* Enter the number of rows and columns of the first matrix separated by a space only. **Note:** Only square, invertible matrices have inverses.
* The program will prompt one row at a time; enter each number separated by a space.
* If the matrix is invertible, the inverse will be displayed in matrix format. If not, an error message will appear.

### **RREF**
* Select option 7 to perform rref operation on a matrix.
* Enter the number of rows and columns of the first matrix separated by a space only (e.g. for 2x3 matrices, enter `2 3`).
* The program will prompt one row at a time; enter each number separated by a space. 
* The program will display step-by-step row reduction operations:
  - Initial matrix
  - Each operation with description (e.g. "R2 → R2 - (3.0)R1")
  - Resulting matrix after each step
  - Final RREF result