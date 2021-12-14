#(6)Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
try:
    lst=[]
    n=int(input("enter size of list:-"))
    for i in range(n):
        print("enter {} element of list".format(i))
        item=int(input())
        lst.append(item)

    print(lst)
    rlst=lst[::-1]
    print(rlst)
    if lst==rlst:
        print("list is palindrome.")
    else:
        print("list is not palindrome.")

except:
    print("enter valid input.i.e=integer value.")