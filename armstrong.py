num=int(input("enter a number:"))
sum=0
# length = len(num)
count = 0
while(num > 0):
    last = num % 10
    count = count + 1
    num = num // 10
    
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**count
    temp=temp//10
if sum==num:
    print("armstrong number")
else:
    print("not armstrong number")
        