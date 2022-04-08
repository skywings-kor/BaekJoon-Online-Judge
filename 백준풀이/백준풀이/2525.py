a,b=input().split()
time=input()

a=int(a)
b=int(b)
time=int(time)

i=0
for i in range(time):
    b=b+1
    
    if(b>59):
        a=a+1
        b=0
        if(a>23):
            a=0


print(a,b)