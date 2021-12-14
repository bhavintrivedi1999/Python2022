#(4)Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
try:
    n=int(input("enter integer number:-"))
    lst=[]
    for i in range(1,n):
        if n%i==0:
            lst.append(i)
    print(lst)
except:
    print("please enter integer number.")