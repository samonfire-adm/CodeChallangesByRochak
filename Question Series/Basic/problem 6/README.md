
# Python Program: Calculate Total and Average Marks

## Problem Statement
This problem involves writing a Python program to calculate the total and average marks of six subjects entered by the user. The program should prompt the user to input marks for six subjects, compute the total marks, and then calculate the average marks. Finally, the program should display the total and average marks to the user.

## How to Solve
To solve this problem, follow these steps:

1. **Prompt User for Input**: Use a loop to ask the user to enter marks for six subjects. Validate the input to ensure that the marks are between 0 and 100.

2. **Calculate Total Marks**: Sum the marks obtained in all six subjects.

3. **Calculate Average Marks**: Divide the total marks by the number of subjects (6) to get the average.

4. **Display Results**: Print the total and average marks to the user.

### Example Code
Here's a sample implementation of the solution:

```python
# Function to get marks from the user
def get_marks(subject_number):
    while True:
        try:
            marks = float(input(f"Enter marks for subject {subject_number}: "))
            if 0 <= marks <= 100:  # Assuming marks are out of 100
                return marks
            else:
                print("Marks should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# List to store marks
marks_list = []

# Get marks for 6 subjects
for i in range(1, 7):
    marks = get_marks(i)
    marks_list.append(marks)

# Calculate total and average
total_marks = sum(marks_list)
average_marks = total_marks / 6

# Display the results
print("\nResults:")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
```

## Solution
[Link to the solution code](#)

## Video Solution
[Link to the video explanation](#)

## Homework Question
Extend the program to handle the following:

1. Calculate the total and average marks for a dynamic number of subjects (ask the user how many subjects).
2. Display a grade based on the average marks:
   - A for average marks >= 90
   - B for average marks >= 80
   - C for average marks >= 70
   - D for average marks >= 60
   - F for average marks < 60

```python
# Extend the solution to handle dynamic number of subjects and display grades

# Function to get marks from the user
def get_marks(subject_number):
    while True:
        try:
            marks = float(input(f"Enter marks for subject {subject_number}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Get the number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# List to store marks
marks_list = []

# Get marks for the specified number of subjects
for i in range(1, num_subjects + 1):
    marks = get_marks(i)
    marks_list.append(marks)

# Calculate total and average
total_marks = sum(marks_list)
average_marks = total_marks / num_subjects

# Determine grade
if average_marks >= 90:
    grade = 'A'
elif average_marks >= 80:
    grade = 'B'
elif average_marks >= 70:
    grade = 'C'
elif average_marks >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display the results
print("\nResults:")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Grade: {grade}")
```

## Solution
[Link to the solution code](#)

## Video Solution
[Link to the video explanation](#)