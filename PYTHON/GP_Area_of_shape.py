print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
pi=3.14
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        radius = float(input("Enter radius: "))
        area = pi * radius * radius
        print("Area of circle:", area)
    elif choice == 2:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print("Area of rectangle:", area)
    elif choice == 3:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Area of triangle:", area)
    else:
        print("Invalid choice")
        break