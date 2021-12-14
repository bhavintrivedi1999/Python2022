#(15)Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
try:
    def rString():
        str=input("enter multiple word string:-")
        lst=str.split(" ")
        rlst=lst[::-1]
        rstr="".join(rlst)
        print(rlst)

    rString()
except:
    print("enter valid input.")
