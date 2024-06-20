# Write a Python Program to Calculate the Area Of circle using formulae πr2
#solution 1
user = int(input("Enter the radius "))
area = 3.14*user*user #pi = 3.14
print(f"The area of circle is {area} m2")

#solution 2
area = lambda r :3.14*r*r
print(str(area(5)) + " m2")