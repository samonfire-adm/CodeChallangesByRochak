# Write a Python Program to Calculate the Area Of rectangle using formulae L x B
# solution 1
length = int(input("Enter the length "))
breadth = int(input("Enter the breadth "))

area = length * breadth
print(f" The area of rectangle is {area} m2")

#Solution 2 
area = lambda l,b:l*b
print(str(area(5,3)) + "m2")