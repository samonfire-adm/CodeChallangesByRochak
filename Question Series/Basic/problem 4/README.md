

# Write A Program That Performs All Arithmetic Operations On Two Variables

## Problem Description

Create a Python program that performs all basic arithmetic operations (addition, subtraction, multiplication, division, and modulus) on two variables. The program should prompt the user to enter two numbers, then display the results of each arithmetic operation.

### Detailed Requirements

1. **Input**:
   - The program should prompt the user to enter two numbers (integers or floats).

2. **Processing**:
   - The program should perform the following arithmetic operations on the two numbers:
     - Addition
     - Subtraction
     - Multiplication
     - Division
     - Modulus

3. **Output**:
   - The program should display the results of each operation in a clear and formatted manner.

### Example

**Input:**
```
Enter the first number: 10
Enter the second number: 3
```

**Output:**
```
Addition: 10 + 3 = 13
Subtraction: 10 - 3 = 7
Multiplication: 10 * 3 = 30
Division: 10 / 3 = 3.3333333333333335
Modulus: 10 % 3 = 1
```

### Additional Considerations

- Ensure the program handles invalid inputs gracefully, such as non-numeric values.
- Handle division by zero with an appropriate error message.

```python
def arithmetic_operations():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print(f"Addition: {num1} + {num2} = {num1 + num2}")
        print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
        print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
        print(f"Division: {num1} / {num2} = {num1 / num2}" if num2 != 0 else "Division by zero is not allowed")
        print(f"Modulus: {num1} % {num2} = {num1 % num2}" if num2 != 0 else "Modulus by zero is not allowed")

    except ValueError:
        print("Please enter valid numbers")

arithmetic_operations()
```
 - Solution is been Uploaded already on YT 
 - Link Is As follow: 
 - And also Code solution is been updated [here](https://github.com/samonfire-adm/CodeChallangesByRochak/blob/main/Question%20Series/Basic/problem%202/main.py) 

## Homework Task

### Write A Program That Performs All Arithmetic Operations On Three Variables

## Problem Description

Create a Python program that performs all basic arithmetic operations (addition, subtraction, multiplication, division, and modulus) on three variables. The program should prompt the user to enter three numbers, then display the results of each arithmetic operation involving these numbers.

### Detailed Requirements

1. **Input**:
   - The program should prompt the user to enter three numbers (integers or floats).

2. **Processing**:
   - The program should perform the following arithmetic operations on the three numbers:
     - Addition
     - Subtraction
     - Multiplication
     - Division
     - Modulus

3. **Output**:
   - The program should display the results of each operation in a clear and formatted manner.

### Example

**Input:**
```
Enter the first number: 10
Enter the second number: 3
Enter the third number: 2
```

**Output:**
```
Addition: 10 + 3 + 2 = 15
Subtraction: 10 - 3 - 2 = 5
Multiplication: 10 * 3 * 2 = 60
Division: 10 / 3 / 2 = 1.6666666666666667
Modulus: 10 % 3 % 2 = 1
```

### Additional Considerations

- Ensure the program handles invalid inputs gracefully, such as non-numeric values.
- Handle division by zero with an appropriate error message.

```python
def arithmetic_operations_three():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        print(f"Addition: {num1} + {num2} + {num3} = {num1 + num2 + num3}")
        print(f"Subtraction: {num1} - {num2} - {num3} = {num1 - num2 - num3}")
        print(f"Multiplication: {num1} * {num2} * {num3} = {num1 * num2 * num3}")
        
        if num2 != 0 and num3 != 0:
            print(f"Division: {num1} / {num2} / {num3} = {num1 / num2 / num3}")
        else:
            print("Division by zero is not allowed")

        if num2 != 0 and num3 != 0:
            print(f"Modulus: {num1} % {num2} % {num3} = {num1 % num2 % num3}")
        else:
            print("Modulus by zero is not allowed")

    except ValueError:
        print("Please enter valid numbers")

arithmetic_operations_three()
```

These solutions should cover the main task and the homework question, ensuring that both handle invalid inputs and division by zero appropriately.

 - Solution is been Uploaded already on YT 
 - Link Is As follow: 
 - And also Code solution is been updated [here](https://github.com/samonfire-adm/CodeChallangesByRochak/blob/main/Question%20Series/Basic/problem%202/main.py) 