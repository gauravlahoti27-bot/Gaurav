a=0
x=0
b=1
z=0
n=int(input("enter number of elements to be printed: "))
while x<n:
    print(a,end="")
    a,b=b,a+b
    x+=1
