import pyfiglet #library to format the text on terminal 
import exception as e
from matrix import Matrix

class Helper:
    """ A helper class for various utility functions """

    @staticmethod
    def show_welcome_message():
        """ Display a welcome message """
        print()
        text = pyfiglet.figlet_format("Welcome to Algebrator", font = "banner3-D", width = 110, justify = "center")
        print(text)


    @staticmethod
    def show_main_menu():
        """ Display the main menu """
        print("\nPlease choose one of the following matrix operations (e.g. for addition, enter 1): ")
        for i in range(len(Operation.operation_list)):
            print(f"{i+1} : {Operation.operation_list[i]}")
        print("\nTo quit the program, press Ctrl + C\n")
            

    @staticmethod
    def show_sub_menu(option):
        """ Display sub-menu based on user option """
        option = option.strip()
        if not option.isnumeric() or 1 > int(option) or len(Operation.operation_list) < int(option):
            raise e.InvalidOptionError("Invalid Option! Please restart the program and choose a valid option from the menu.")
        
        print("-" * 60, "\n")

        match int(option):
            case 1:
                print("You chose Addition")
                print("Please enter the matrices to be added by following the prompts carefully\n")
                result = Operation.addition()
                print("\nResult:")
                print(result)

            case 2:
                print("You chose Subtraction")
                print("Please enter the matrices to be subtracted by following the prompts carefully\n")
                result = Operation.subtraction()
                print("\nResult:")
                print(result)

            case 3:
                print("You chose Multiplication")
                print("Please enter the matrices to be multiplied by following the prompts carefully")
                print("(Note: Number of columns in the first matrix must equal number of rows in the second matrix)\n")
                result = Operation.multiplication()
                print("\nResult:")
                print(result)

            case 4:
                print("You chose Determinant")
                print("Please enter the matrix to find the determinant by following the prompts carefully")
                print("(Note: Only square matrices have determinants)\n")
                result = Operation.determinant()
                print("\nResult:")
                print(result)

            case 5:
                print("You chose Transpose")
                print("Please enter the matrix to be transposed by following the prompts carefully\n")
                result = Operation.transpose()
                print("\nResult:")
                print(result)

            case 6:
                print("You chose Inverse")
                print("Please enter the matrix to be inverted by following the prompts carefully")
                print("(Note: Only square matrices with non-zero determinant can be inverted)\n")
                result = Operation.inverse()
                print("\nResult:")
                print(result)

            case 7:
                print("You chose Row-reduce-echelon-form")
                print("Please enter the matrix to be row-reduced to echelon form by following the prompts carefully\n")
                result = Operation.row_reduce_echelon()
                print("\nResult:")
                print(result)
                

    @staticmethod
    def do_again():
        """ Ask user if they want to perform another operation """
        choice = input("\nWould you like to try again? (y/n): ").lower()
        return choice == 'y'
    
    
    @staticmethod
    def exit_message():
        """ Display an exit message """
        print("\nThank you for using Algebrator! Goodbye!\n")


class Operation:
    """ A class to handle various matrix operations """
    
    operation_list = [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Determinant",
        "Transpose",
        "Inverse",
        "Row-reduce-echelon-form",
    ]
    def _get_matrix_size():
        """ Get matrix size from user input """

        try:
            rows, cols = input("Please enter number of rows and columns separated by a space: ").strip().split(" ")
        except ValueError:
            raise e.InvalidInputError("Rows and columns must be positive integers separated by a space only")
        
        if not (rows.isdigit() and cols.isdigit()):
            raise e.InvalidInputError("Rows and columns must be positive integers separated by a space only")
        if int(rows) < 1 or int(cols) < 1 or int(rows) > 10 or int(cols) > 10:
            raise e.MatrixSizeError("Rows and columns must be between 1 and 10, inclusive")
        return int(rows), int(cols)

    def _get_matrix_data(rows, cols):
        """ Get matrix data from user input """

        print(f"Please enter the matrix data row by row, with each element separated by a space:")
        data = []
        for i in range(rows):
            row_data = input(f"\tRow {i+1}: ").split()
            try:
                row_data = [float(x) for x in row_data]
            except ValueError:
                raise ValueError("Matrix elements must be numeric values")
            
            if len(row_data) != cols:
                raise e.MatrixDimensionError("Number of elements in the row does not match the specified number of columns")
            data.append(row_data)
        return data

    @staticmethod
    def addition():
        """ Perform matrix addition """

        try:
            rows, cols = Operation._get_matrix_size()

            print(f"\n\nMatrix 1: ({rows} x {cols})")
            m1 = Matrix(rows, cols)
            m1.set_data(Operation._get_matrix_data(rows, cols))

            print(f"\nMatrix 2: ({rows} x {cols})")
            m2 = Matrix(rows, cols)

            m2.set_data(Operation._get_matrix_data(rows, cols))

        except (e.MatrixSizeError, e.MatrixDimensionError, e.InvalidInputError, ValueError) as ex:
            print(f"\nError: {ex}")
            return None

        return m1 + m2

    @staticmethod
    def subtraction():
        """ Perform matrix subtraction """

        try:
            rows, cols = Operation._get_matrix_size()
            print(f"\n\nMatrix 1: ({rows} x {cols})")
            m1 = Matrix(rows, cols)
            m1.set_data(Operation._get_matrix_data(rows, cols))

            print(f"\nMatrix 2: ({rows} x {cols})")
            m2 = Matrix(rows, cols)

            m2.set_data(Operation._get_matrix_data(rows, cols))
        except (e.MatrixSizeError, e.MatrixDimensionError, e.InvalidInputError, ValueError) as ex:
            print(f"\nError: {ex}")
            return None

        return m1 - m2

    @staticmethod
    def multiplication():
        """ Perform matrix multiplication """

        try:
            print("First Matrix:", end=" ")
            row1, col1 = Operation._get_matrix_size()
            print(f"\n\nMatrix 1: ({row1} x {col1})")
            m1 = Matrix(row1, col1)
            m1.set_data(Operation._get_matrix_data(row1, col1))

            print()
            print("Second Matrix:", end=" ")
            row2, col2 = Operation._get_matrix_size()

            if col1 != row2:
                raise e.MatrixDimensionError("Number of columns in the first matrix must equal number of rows in the second matrix!")
            
            print(f"\nMatrix 2: ({row2} x {col2})")
            m2 = Matrix(row2, col2)
            m2.set_data(Operation._get_matrix_data(row2, col2))

        except (e.MatrixSizeError, e.MatrixDimensionError, e.InvalidInputError, ValueError) as ex:
            print(f"\nError: {ex}")
            return None

        return m1 * m2

    @staticmethod
    def determinant():
        """ Calculate the determinant of a matrix """

        try:
            rows, cols = Operation._get_matrix_size()
            if rows != cols:
                raise e.MatrixDimensionError("Only square matrices have determinants")
            
            print(f"\n\nMatrix: ({rows} x {cols})")
            m = Matrix(rows, cols)
            m.set_data(Operation._get_matrix_data(rows, cols))
            return round(m.determinant(), 4) # round to 4 decimal pt to avoid precision error
        except (e.MatrixDimensionError, e.InvalidInputError, ValueError) as ex:
            print(f"\nError: {ex}")
            return None

    @staticmethod
    def transpose():
        """ Transpose a matrix """

        try:
            rows, cols = Operation._get_matrix_size()
            print(f"\n\nMatrix: ({rows} x {cols})")
            m = Matrix(rows, cols)
            m.set_data(Operation._get_matrix_data(rows, cols))
        except (e.MatrixSizeError, e.MatrixDimensionError, e.InvalidInputError, ValueError) as ex:
            print(f"\nError: {ex}")
            return None
        
        return m.transpose()

    @staticmethod
    def inverse():
        """ Calculate the inverse of a matrix """

        try:
            rows, cols = Operation._get_matrix_size()
            if rows != cols:
                raise e.MatrixDimensionError("Only square matrices have inverses")
            
            print(f"\n\nMatrix: ({rows} x {cols})")
            m = Matrix(rows, cols)
            m.set_data(Operation._get_matrix_data(rows, cols))
            return m.inverse()
        except (e.MatrixSizeError, e.MatrixDimensionError, e.MatrixNotInvertibleError, e.InvalidInputError, ValueError) as ex:
            print(f"\nError: {ex}")
            return None

    @staticmethod
    def row_reduce_echelon():
        """ Row-reduce a matrix to echelon form """

        try:
            rows, cols = Operation._get_matrix_size()
            print(f"\n\nMatrix: ({rows} x {cols})")
            m = Matrix(rows, cols)
            m.set_data(Operation._get_matrix_data(rows, cols))
        except (e.MatrixSizeError, e.MatrixDimensionError, e.InvalidInputError, ValueError) as ex:
            print(f"\nError: {ex}")
            return None
        
        print("\nRow-reduction steps:\n")
        last_step = None
        for step_matrix, description in m.row_reduce_echelon():
            print(description)
            print(step_matrix)
            print()
            last_step = (step_matrix, description)
        return last_step[0]  # Return only the final matrix
        
