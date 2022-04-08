a=input()
b=input()

a=int(a)
b=int(b)

if(0<a and 0<b):
    print("1")

elif(0<a and 0>b):
    print("4")

    
elif(0>a and 0<b):
    print("2")

    
elif(0>a and 0>b):
    print("3")


else:
    print("")