

count=0
lst=[]
n1=int(input('enter starting range:- '))
n2=int(input('enter ending range:-'))

for i in range(n1,n2+1):
    for j in range (2,i):
        if (i%j==0):
            break
           
            
    else:
        lst.append(i)
             
print(lst)

