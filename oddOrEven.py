#(2)Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
try:
    n=int(input("enter integer number:-"))
    if n%2==0:
        print("the number is even.")
    else:
        print("the number is odd.")
except:
    print("please enter integer number.")