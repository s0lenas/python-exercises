# python-exercises
A small collection of Python exercises completed as part of my university curriculum.

## Project Structure

## Detailed Descriptions

### **Assignment1.py**
1. **Exercise 1: Narcissistic Numbers**
    - Calculates and prints all narcissistic numbers between 1 and 600,000.
    - Narcissistic numbers are those where the sum of their digits, each raised to the power of the number of digits, equals the number itself.

2. **Exercise 2: Prime Numbers**
    - Prints prime numbers between 2 and 1000, 20 per line.

3. **Exercise 3: Greatest Common Divisor**
    - Prompts the user for two positive integers and calculates their greatest common divisor using an iterative approach.

4. **Exercise 4: Sine Calculation**
    - Uses the Taylor series expansion to approximate the sine of a user-provided angle (in degrees).
    - Compares the result to Python's built-in `math.sin()` function for accuracy.

---

### **ex1.py**
1. **Palindrome Detection**
    - Part (a): Checks if two user-provided words are palindromes.
    - Part (b): Checks if a user-provided sentence is a palindrome, ignoring spaces and capitalization.
    - Part (c): Combines the above functions to validate user inputs.

---

### **ex2.py**
1. **Random List Generation**
    - Generates two sorted lists of 15 random integers each (between 0 and 100).
    - Combines and sorts the two lists into a single sorted list.

2. **String Sorting**
    - Accepts a user-provided string and returns the characters sorted in ascending order.

---

### **ex3.py**
## Overview
This Python script, `ex3.py`, is designed to manage and manipulate player data stored in a file. It includes functionality for filtering, formatting, and presenting player information in a tabular format. The script also allows users to query, add, or sort players based on specified criteria.

1. **File Handling**
   - Prompts the user to specify a file containing player data.
   - Validates the file and handles errors gracefully.

2. **Data Formatting and Presentation**
   - Converts raw data into formatted tuples and lists.
   - Creates tabular displays with aligned columns.

3. **Data Query Options**
   - Search for a player by last name.
   - Filter players by salary range.
   - List players in a specific team.
   - Find players based on their position and team.
   - Sort players by position and salary range in ascending order.

4. **Data Modification**
   - Add new players to the dataset while validating input criteria.

5. **Error Handling**
   - Handles input errors, such as invalid file names or data that doesn't meet constraints.

---

## Requirements
- Python 3.x
- Standard Python libraries (`math`, `random`)