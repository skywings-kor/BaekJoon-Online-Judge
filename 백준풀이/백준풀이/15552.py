import sys
a=input()
a=int(a)

for i in range(1,a+1):
    num1,num2=map(int,sys.stdin.readline().split())
    print(num1+num2)
