print("1. Rupees to Dollar")
print("2. Celsius to Fahrenheit")
print("3. Inches to Feet")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        rupees = float(input("Enter amount in rupees: "))
        dollars = rupees / 83
        print("Amount in dollars:", dollars)
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
    elif choice == 3:
        inches = float(input("Enter inches: "))
        feet = inches / 12
        print("Feet:", feet)
    else:
        print("Invalid choice")
    break