n = int(input("Enter a number: "))
sum = 0
dn = n
i = 0
while i < n:
    n = n % 10
    dn = dn // 10
    i += 1
if n == dn:
    print("Palindrome")
else:
    print("Not a palindrome")