n = int(input("Enter a number: "))
a = int(input("Enter n: "))

# Upper part
for i in range(0, n + 1):
    print("*" * (n - i) + " " * (2*i) + "*" * (n - i))

# Lower part
for i in range(1, a + 1):
    print("*" * i + " " * (2*(n - i)) + "*" * i)