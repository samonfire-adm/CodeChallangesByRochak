def cococola(n):
    for i in range(1,n+1):
        if i%3 ==0 and i%5==0 :
            print("COCOCOLA")
        elif i%3 ==0:
            print("Coca")
        elif i%5 ==0:
            print("Cola")
        else:
            print(i)

print(cococola(15))