f=int(input())
a=str(input())
b=list(a[ : :-1])
for i in b:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        b.remove(i)
print("".join(b))




