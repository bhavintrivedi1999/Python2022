# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153
num=int(input('enter number:-'))


#checking len of num
n=len(str(num))
# print(n)

temp=num
sum=0
#checking armstrong
while(temp!=0):
    l=temp%10
    sum+=l**n
    temp=temp//10

if (sum==num):
    print('number is armstrong.')
else:
    print("not armstrong.")























