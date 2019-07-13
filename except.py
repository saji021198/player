d=int(input())
a=list(map(int,input().split()))
sum=1
for i in a:
    if a.count(i)==sum:
        sum=a.count(i)
        max=i
print(max)


