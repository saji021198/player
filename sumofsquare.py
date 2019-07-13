a=int(input())
sum=0
v=a
while v>0:
    z=v%10
    v=v//10
    sum=sum+pow(z,2)
print(sum)
