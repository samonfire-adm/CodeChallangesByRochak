# Problem Number 1


## Problem Statement

Write a Python program to display a table of numbers and their squares in a specific layout.

### Expected Output

The program should generate a table with two columns: "Numbers" and "Square". Each row in the table should display a number and its square. Here is the expected output format:

Numbers         Square
1               1
2               4
3               9
4               16
...             ...
## How It Works
The function generate_table(n) takes an integer n as an argument, which specifies the range of numbers to display.
It prints the headers "Numbers" and "Square" with a fixed width using formatted strings.
It then iterates through the range from 1 to n, printing each number and its square in a tabular format.