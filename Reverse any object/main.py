def reverse_string(input_string):
    stack = []
    for char in input_string:
        stack.append(char)  
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    return reversed_string

# Test the function
input_string = input("Enter the object to be reversed")
reversed_string = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)
