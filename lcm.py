k,l=map(int,input().split())
t=[]
m=[]
lcm=1
r=max(k,l)
for i in range(1,r):
    if(k%i==0 and l%i==0):
        t.append(i)
        k=k//i
        l=l//i
m.append(k)
m.append(l)
for u in t:
    lcm=lcm*u
for r in m:
    lcm=lcm*r
print(lcm)
        
        
