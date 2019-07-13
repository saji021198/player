a,b=map(int,input().split())
z=list(map(int,input().split()))
for i in range (0,b):
    z=[z[-1]]+z[:-1]
print(*z,end='')
