#(14)Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
try:
    lst=[]
    n=int(input("size of list:-"))
    for i in range(n):
        item=input("enter list element of index {}:-".format(i))
        lst.append(item)


    def reDup(lst):
        nlst=set(lst)
        lst=list(nlst)
        print(lst)

    reDup(lst)
except:
    print("enter valid input.")