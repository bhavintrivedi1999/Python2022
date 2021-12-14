#(11)Ask the user for a number and determine whether the number is prime or not.
try:
    count=0
    n=int(input("enter integer:-"))
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==0:
        print("prime number.")
    else:
        print("not prime number.")
except:
    print("enter valid integer input.")
