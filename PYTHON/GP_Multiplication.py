n = int(input("Enter a number to generate table configuration: "))
for i in range(1,11):
    print(f"{n:>2} X {i:>2} = {n*i:>2}")
