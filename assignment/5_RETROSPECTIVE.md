# Project Retrospective

Retrospectives are an excellent opportunity for your agile team to evaluate itself and create a plan to address areas of improvement for the future. The [retrospective](https://www.atlassian.com/agile/scrum/retrospectives) embraces the ideal of continuous improvement - and protects against the pitfalls of complacency - by stepping outside the work cycle to reflect on the past.

Your task here will be to answer the following two areas where it says YOUR ANSWER HERE:

---

## Identify your Successes and Improvements

Create a short list of things that were **successful** and worked well, then also things that could be **improved**. You must have a minimum of 2 items for each. Focus this section on the **technical** successes and improvements of the project.

### Your Successes

* **Robust Error Handling and Input Validation** - The program successfully handles all edge cases and invalid inputs gracefully. All custom exception classes (`MatrixSizeError`, `InvalidOptionError`, `MatrixDimensionError`, `MatrixNotInvertibleError`, `InvalidInputError`) work correctly and provide meaningful error messages to users. The system never crashes on invalid input and always guides users toward correct usage, whether dealing with dimension mismatches, non-numeric inputs, or mathematical errors like inverting zero-determinant matrices.

* **Step-by-Step RREF Implementation** - Successfully implemented the RREF operation with a generator that yields each row operation step, allowing users to understand the transformation process rather than just seeing the final result. This educational feature enhances the learning value of the calculator by showing row operations like `R2 -> R2 - 3 * R1` with the resulting matrix after each step.

* **Modularity and Maintainable Code Structure** - Organized the code into logical modules (Matrix class, exception classes, helper module, and main program) following object-oriented design principles. Implemented operator overloading (`+`, `-`, `*`) for intuitive matrix operations and included a clean `__repr__` method for consistent matrix display throughout the program.

### Your Improvement

* **Matrix Display Formatting** - Currently, all matrix elements are displayed as decimals (e.g. `0.3333`), which can be less readable for operations like matrix inversion and rref that often produce fractions. Implementing an option to display results as simplified fractions (e.g `1/3` instead of `0.3333`) would improve readability and better align with how these results are typically presented in linear algebra textbooks.

* **Limited Operation Set** - While the calculator covers fundamental matrix operations (addition, subtraction, multiplication, transpose, determinant, inverse, and RREF), it lacks more advanced operations commonly needed in linear algebra courses. Adding operations such as calculating matrix rank, eigenvalues and eigenvectors, would make the calculator more comprehensive and useful for a wider range of problems and coursework.

* **No File I/O Capabilities** - The program currently requires users to manually input all matrix data each time they run the program, which is inefficient for working with the same matrices repeatedly or for larger matrices. Implementing the ability to save matrices to files (e.g. `.txt`, `.csv`, or `.json` formats) and load them back into the program would significantly improve workflow efficiency and allow users to export the calculated results to reduce the repeated calculation.

* **Lack of Undo and History Functionality** - Once a user completes an operation, there is no way to go back or undo their last action without restarting the program and reentering all data. Implementing an operation history with undo capabilities would greatly enhance user experience, especially when users make mistakes in matrix entry or want to compare results from different operations on the same matrix without reentering data multiple times.

---

## Improving Yourself for the Future

Discuss ways and tactics to improve yourself that will lead to the improvement of the items on the "Your Improvement" list. Focus on outcomes, not actions, technology, or people, or the past.

* To add more operations into it, I will expand my knowledge of linear algebra algorithms beyond the fundamentals by studying more advanced topics such as eigenvalue decomposition and probably vector space. This includes understanding both the mathematical theory and practical implementation considerations for these algorithms. This will enhance my ability to build more comprehensive mathematical tools that serve a broader range of academic use cases.

* I will develop a deeper understanding of data presentation strategies by studying how to implement dual-mode output systems that can switch between different representations (fractions vs. decimals) based on context or user preference. This will involve learning about fraction simplification algorithms, greatest common divisor calculations, and when to apply each display format. It will improve the ability to design flexible output systems that adapt to user needs and enhance readability, which makes this project in the future more user-friendly.

* I will also strengthen my skills in data and file handling by learning best practices for serializing and deserializing complex data structures, designing file format plans, and implementing error handling for file I/O operations. This includes studying different file formats (CSV, JSON), understanding when each is appropriate, and learning to handle edge cases like corrupted files or invalid data. From this, I will learn how to integrate with users' workflows by allowing them to save and retrieve their work that significantly improving usability and making this project more practical for real-world use.
