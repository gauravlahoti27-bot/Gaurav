n=int(input("enter number to be analysed:"))
flag=True
for x in range(2,n):
    if n%x==0:
        print("not prime")
        flag=False
        break
    else:
        pass
if flag==True:
    print("prime")
else:
    pass
