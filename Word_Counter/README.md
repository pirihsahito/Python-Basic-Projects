# Simple Word Counter (Manual & File-Based)

This is a beginner-friendly command-line tool built with Python that counts the total number of words in any text. It gives you two choices: you can either paste text directly into the terminal or tell it to open and read an entire text file from your computer.

---

## How it Works (In Simple Words)

This project introduces two powerful intermediate Python skills: breaking down sentences and working with external files.

### 1. The Counting Machine (`.split()` and `len()`)
Inside the `word_count()` function, Python counts words using a simple two-step trick:
* `text.split()` takes a long string of text and cuts it up wherever there is a space, turning it into a Python list of individual words.
* `len(words)` calculates the "length" of that list, which tells you exactly how many words were in the text.

### 2. Reading External Files Safely
The `file_count()` function handles opening files from your computer. 
* **The Smart Open (`with open`):** Using the `with` keyword is like hiring a polite assistant. It opens the file, lets Python read the text inside it, and automatically closes it when finished so your computer's memory stays clean.
* **The Lost File Safety Net (`except FileNotFoundError`):** If you type a filename that doesn't exist (like misspelling `notes.txt` as `nets.txt`), standard Python will panic and crash. This code uses a `try/except` safety net to catch that specific mistake, print a friendly reminder to check the spelling, and keep the application running.

### 3. The Control Center Menu (While Loop)
A continuous `while True` loop drives the user interface. It presents a simple menu asking you to press `1` for manual typing, `2` for a file search, or `q` to quit. If you type anything else, the `else:` branch handles the mistake smoothly without breaking the application structure.

---

## How to Use It

1. Run the script in your terminal.
2. Select an option from the main menu:
   * **Press 1:** Paste or type a sentence directly into the terminal to get an immediate word count.
   * **Press 2:** Type the exact name of a text file (e.g., `essay.txt`) located in the same folder as your script to count its words.
   * **Press q:** Instantly close the application.

---

## Example Outputs

### Mode 1: Manual Input
```text
Press 1 to enter text manually, Press 2 to read a text file, or Press 'q' to exit: 1
Paste your text here: Python is an amazing programming language.
The number of words are:  6

```

### Mode 2: Missing File Handling

```text
Press 1 to enter text manually, Press 2 to read a text file, or Press 'q' to exit: 2
Write the name of file here: missing_document.txt
Write the correct name of file.

```