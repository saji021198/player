d,a=map(int,input().split())
w=d
r=a
if(d>a):
    while(d>0):
        if((d%a)==0 and (d%w)==0):
            print(d)
            break
        else:
            d=d+1
    
else:
    while(a>0):
        if((a%d)==0 and (a%r)==0):
            print(a)
            break
        else:
            a=a+1
