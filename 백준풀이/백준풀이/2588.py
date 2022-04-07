a=int(input())
b=int(input())

num4=b/100
num4=int(num4)
b=b-(num4*100)

num5=b/10
num5=int(num5)
b=b-(num5*10)



num6=b/1
num6=int(num6)
b=b-(num6*1)


print(a*num6)
print(a*num5)
print(a*num4)

res1=a*num5*10
res2=a*num4*100

print(a*num6+res1+res2)
