#!  Write A Python Program To Take Marks From The User To Check Whether User Able To Admission In College Or Not. If Marks Is Less Than 60 Then It Don't Allow To Take Admission.

def checker():
    try:
        marks= float(input("Enter the marks in numbers: "))
        print("User is able to take admission in school " if marks >= 60 else "User is not allowed to take admission ")
    except ValueError:
        print("Enter the valid value in numbers ")

checker()
