# Simple Python Calculator

This is a beginner-friendly command-line calculator built with Python. It can add, subtract, multiply, and divide numbers. The best part? It is built defensively, meaning it won't crash if you make a typing mistake!

---

## How it Works (In Simple Words)

This project uses three major building blocks of Python:

### 1. The Math Brain (Functions)
At the top, we created a custom box called `calculate()`. You give this box two numbers and a symbol (like `+` or `-`). It looks at the symbol, does the math, and throws the answer back to you. 
* **Special Safety Feature:** If you try to divide a number by `0`, the brain stops and gives you an error message instead of letting the program crash.

### 2. The Safety Net (Try / Except)
Normally, if you ask Python to turn text like `"apple"` into a number, the program completely stops and crashes. We wrapped our inputs in a **`try/except`** safety net. If a user types text instead of a number, Python drops into the `except` block, prints a nice warning message, and keeps going.

### 3. The Continuous Loop (While Loop)
We used `while True` to create a loop that keeps the calculator running over and over again. You don't have to restart the script after every calculation. It will keep asking for numbers until you explicitly type `q` to quit, which triggers the `break` command to stop the machine.

---

## How to Use It

1. Run the script in your terminal.
2. Enter your first number.
3. Enter your second number.
4. Type the math symbol you want to use:
   * `+` for Addition
   * `-` for Subtraction
   * `*` or `x` for Multiplication
   * `/` for Division
5. View your result!
6. Press `q` to exit, or press any other key to do another calculation.

---

## Code Logic Flow

* **Inputs gathered** $\rightarrow$ Checked by the **Safety Net** (Checks for invalid text).
* **Inputs sent to the Brain** $\rightarrow$ Checked by **Math Logic** (Checks for division by zero or invalid symbols).
* **Result printed** $\rightarrow$ User chooses to **Continue or Quit**.
