import pdb
def calculate_average(a, b):
    total = a + b
    avg = total / c   # Intentional error: variable c not defined
    return avg

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = calculate_average(x, y)
print("Average =", result)
