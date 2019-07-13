a=str(input())
sum=0
for i in a:
    if a.count(i)>sum:
        sum=a.count(i)
        max=i
print(max)

