#(13)Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
try:
    n=int(input("how many fibonnaci number want to generate here:-"))
    t1=0
    t2=1
    for i in range(n):
        # 1,1,2,3,5,8,13
        
        print(t2)
        t3=t1+t2
        t1=t2
        t2=t3
except:
    print("enter valid integer input.")

