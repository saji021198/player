a=int(input())
l=[]
for i in range (2,a+1):
    if(a%i)==0:
        l.append(i)
        a=a//i
s=sorted(l)
print(*s)
        
        
    
