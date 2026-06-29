n = int(input("Enter a number: "))

num = str(n)
if len(num)%2 != 0:
    print("Not a tech no.")
else:
    mid_num = len(num)//2
    first = int(num[:mid_num])
    second = int(num[mid_num:])

    sum = first + second
    if sum**2 == n:
        print("Tech no.")
    else:
        print("Not a tech no.") 