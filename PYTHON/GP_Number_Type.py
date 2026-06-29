while True:
    num = int(input("Enter a Number :"))
    if num%2==0:
        print("is even")
    else :
        print("is odd")
    choice = input("do you want to check another number(y/n): ")
    if choice.lower()=="n":
        break
