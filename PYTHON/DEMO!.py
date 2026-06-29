Extra codes for pyhton exam
===========================================================
my_dict = {"a": 1, "b": 2, "c": 3}

key = input("Enter key to check: ")

if key in my_dict:
    print("Key exists")
else:
    print("Key does not exist")



for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)

=========================================================

def compound_interest(p, r, t):
    amount = p * (1 + r/100) ** t
    ci = amount - p
    return ci

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Compound Interest:", compound_interest(p, r, t))

==========================================================

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

calc = Calculator()

print(calc.add(10, 5))
print(calc.subtract(10, 5))
print(calc.multiply(10, 5))
print(calc.divide(10, 5))

============================================================

def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

numbers = [2, 3, 4]
print(multiply_list(numbers))

============================================================

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

============================================================

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD:", gcd(num1, num2))

===========================================================

string = input("Enter a string: ")
# Sorting words
words = string.split()
words.sort()
print("Sorted words:", words)

# Counting vowels and consonants
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for char in string:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)

===========================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []

for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)

print("Transpose:")
for row in transpose:
    print(row)

===========================================================

string = input("Enter string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

===========================================================
