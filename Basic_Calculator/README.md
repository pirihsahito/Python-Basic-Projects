# Task 1: Simple Command-Line Calculator

A robust command-line calculator developed using Python as part of the SAM AI Technologies Internship program. This application prompts users for two numbers and an arithmetic operator, executing the calculation safely while actively preventing runtime crashes.

## Features
- **Basic Arithmetic:** Supports addition, subtraction, multiplication, and division.
- **Robust Exception Handling:** Catches type conversion errors safely if non-numeric values are inputted.
- **Defensive Design:** Actively prevents program termination due to runtime edge cases like Zero Division.

## Concepts Practiced
- **Control Flow:** Utilized conditional `if-elif-else` branching to direct execution paths.
- **Error Handling:** Implemented `try-except` statements targeting `ValueError` and structural boundary checks.
- **Data Type Casts:** Structured runtime conversion using standard `float()` wrappers to allow decimal accuracy.

## How to Run
1. Ensure Python 3.x is installed on your local environment.
2. Clone this repository or download the source script.
3. Open a terminal/command prompt, navigate to the directory, and execute:
   ```bash
   python main.py