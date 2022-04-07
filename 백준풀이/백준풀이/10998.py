a, b,c = input().split()
a=int(a)
b=int(b)
c=int(c)

resl1=(a+b)%c
resr1=((a%c)+(b%c))%c

resl2=(a*b)%c
resr2=((a%c)*(b%c))%c

print(resl1)
print(resr1)
print(resl2)
print(resr2)
