while True:
    ch=input("Enter a one variable: ")
    if len(ch)!=1:
        print("Enter only one character:")
    elif  ch>='0' and  ch<='9':
        print("It is a digit")
    elif  ch>='a' and 'z':
        print("It is a lower case")
    elif  ch>='A' and 'Z':
        print("It is an upper case")
    else:
        print("It is special character")
    choice = input("do you want to check another character(y/n): ")
    if choice.lower()== "n":
        break
