#   Write A Python Program To Take Age From The User To Check Whether User Able To Participate In Voting Or Not. If Age Is Less Than 18 Then It Don't Allow To Participation. And Show, After How Much Year A Person Will Be Able To Participate:

def checker():
    try:
        age = int(input("Enter the age in numbers "))
        if age <0:
            print("Please Enter positive age")
            return
        if age>= 18:
            print("You are eligible for voting ")
        else:
            year = 18 - age
            print("You are not  eligible for voting")
            print(f"{year} years left for voting you can't participate ")
    except ValueError :
        print("Please Enter Age in Number ")


checker()

#! second solution 

def checker():
    try:
        age = int(input("Enter the age in numbers "))
        # ternary operator 
        if age<0:
            print("Please enter valid age ")
            return
        print("You are eligible for voting" if age>=18 else f"you are not eligible for voting \n{18-age} years are left for participation")
    except ValueError :
        print("Please Enter Age in Number ")


checker()

