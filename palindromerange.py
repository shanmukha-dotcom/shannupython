a=int(input("enter"))
b=int(input("enter"))
for i in range(a,b):
    rev=0
    temp=i
    while i>0:
        d=i%10
        rev=rev*10+d
        i=i//10
    if rev==temp:
        print(rev)    
