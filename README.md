# 🧮 Algebrator

![Language](https://img.shields.io/badge/language-Python-3776AB.svg?logo=python)
![Interface](https://img.shields.io/badge/interface-CLI-black.svg)


A command-line linear algebra calculator built in Python with step-by-step walkthroughs for every operation. Enter a matrix, pick an operation, and watch Algebrator solve it one step at a time.

---

## Table of Contents

- [Features](#features)
- [Supported Operations](#supported-operations)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example Session](#example-session)
- [Running Tests](#running-tests)
- [Contributing](#contributing)

---

## Features

- Performs common linear algebra matrix operations via an interactive CLI menu
- Displays every intermediate step of row reduction, making it useful as a study tool
- Supports matrices up to **10 × 10** in size
- Built-in error handling for invalid dimensions, non-invertible matrices, and bad input
- Zero external dependencies — runs on pure Python

---

## Supported Operations

| Operation | Details |
|---|---|
| **Matrix Addition** | Adds two same-dimension matrices |
| **Matrix Subtraction** | Subtracts two same-dimension matrices |
| **Matrix Multiplication** | Multiplies two compatible matrices (m×n · n×p) |
| **Transpose** | Flips a matrix over its diagonal |
| **Determinant** | Computes the determinant of any square matrix (recursive cofactor expansion) |
| **Inverse** | Inverts a square matrix using the adjoint method (2×2 shortcut included) |
| **Row Reduction (RREF)** | Reduces a matrix to reduced row echelon form with step-by-step output |

---

## Tech Stack

| Category       | Technology            |
|----------------|-----------------------|
| Language       | Python 3              |
| Interface      | CLI (interactive menu)|
| Testing        | Python `unittest`     |
| Dependencies   | None (standard library only) |

---

## Project Structure

```
Algebrator/
├── main.py            # Entry point — launches the interactive menu
├── matrix.py          # Matrix class with all supported operations
├── helper.py          # Menu display and user input handling
├── exception.py       # Custom exceptions (MatrixSizeError, MatrixDimensionError, etc.)
├── test_matrix.py     # Unit tests for matrix operations
├── draft-1/           # First draft iteration of the project
├── draft-2/           # Second draft iteration of the project
├── assignment/        # Original assignment README and requirements
└── rubric/            # Grading rubrics (instructor and student)
```

---

## Prerequisites

- Python 3.8 or higher
- No external packages required

To check your Python version:
```bash
python3 --version
```

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DyDyVNR/Algebrator.git
   cd Algebrator
   ```

2. **Run the program** (no install step needed)
   ```bash
   python3 main.py
   ```

---

## Usage

After launching, Algebrator presents an interactive menu:

```
========================================
       Welcome to ALGEBRATOR
========================================

Main Menu:
  1. Matrix Addition
  2. Matrix Subtraction
  3. Matrix Multiplication
  4. Transpose
  5. Determinant
  6. Inverse
  7. Row Reduction (RREF)

Enter number here >>
```

Select an operation, then follow the prompts to enter your matrix dimensions and values. For row reduction, each step is printed in sequence — row swaps, scaling, and elimination — so you can follow along with the full solution process.

To quit at any time, press `Ctrl + C`.

---

## Example Session

```
Enter number here >> 7       # Select Row Reduction

Enter number of rows: 3
Enter number of cols: 4

Enter matrix values:
...

Initial matrix:
     1.0      2.0      3.0      4.0
     5.0      6.0      7.0      8.0
     9.0     10.0     11.0     12.0

Swap R1 <-> R1
R1 / 1.00 -> R1
R2 - (5.00)R1 -> R2
R3 - (9.00)R1 -> R3
...

Final Result (RREF):
     1.0      0.0     -1.0     -2.0
     0.0      1.0      2.0      3.0
     0.0      0.0      0.0      0.0
```

---

## Running Tests

Unit tests for the `Matrix` class are in `test_matrix.py`. Run them with:

```bash
python3 -m unittest test_matrix.py -v
```

---

## Contributing

Feel free to fork and extend it with new operations!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-operation`)
3. Commit your changes (`git commit -m 'Add new operation'`)
4. Push to the branch (`git push origin feature/new-operation`)
5. Open a Pull Request

---
