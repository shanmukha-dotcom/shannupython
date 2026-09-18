s=input("enter")
count=0
for ch in s:
    if ch in "aeiouAEIOU":
        count+=1
print("vowles",count)        