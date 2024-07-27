
# Python Program: Validate Password Requirements

## Problem Statement
This program prompts the user to enter a password and ensures that the password meets specific criteria:
- It must contain at least one numeric digit (`0-9`).
- It must contain at least one alphabetic character (`a-z`, `A-Z`).

## How to Solve
To solve the main problem of validating password requirements:

1. **Prompt User for Password**: Ask the user to enter a password.

2. **Validation Requirements**:
   - Use functions to check if the password contains at least one numeric digit and at least one alphabetic character.

3. **Output**: Display a message indicating whether the password meets the criteria or not.

### Example Code
#### Part 1: Validate Password Requirements
```python
# Function to validate password
def validate_password(password):
    has_digit = any(char.isdigit() for char in password)
    has_alpha = any(char.isalpha() for char in password)
    return has_digit and has_alpha

# Get password from user
password = input("Enter your password: ")

# Validate password
if validate_password(password):
    print("Password is valid.")
else:
    print("Password must contain at least one number and one alphabetic character.")
```

## Homework Question
Extend the password validation program to also check:
- The password length should not be greater than or equal to 10 characters.

### Example Code for Homework Question
#### Part 2: Validate Password Length
```python
# Function to validate password length
def validate_password_length(password):
    return len(password) < 10

# Get password from user
password = input("Enter your password: ")

# Validate password length
if validate_password(password):
    if validate_password_length(password):
        print("Password is valid.")
    else:
        print("Password length should be less than 10 characters.")
else:
    print("Password must contain at least one number and one alphabetic character.")
```

## Solution
[Link to the solution code](#)

## Video Solution
[Link to the video explanation](#)
