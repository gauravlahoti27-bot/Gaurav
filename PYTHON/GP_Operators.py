a=int(input("enter first number:"))
b=int(input("enter second number:"))
opcode=int(input("menu\n1:addition\n2:subtraction\n3:multiplication\n4:division\n:\t"))
match opcode:
    case 1:
        print(f"addition of a and b={a+b}")
    case 2:
        print(f"subtraction of b from a={a-b}")
    case 3:
        print(f"multiplication of a and b={a*b}")
    case 4:
        if b==0:
            print("zero division not possible")
        else :
            print(f"division of a by b={a/b}")
    case _:
        print("invalid opcode:")
