try:
    # Taking input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Performing division
    result = num1 / num2

    print("Result =", result)

# Handles division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handles invalid input (like letters instead of numbers)
except ValueError:
    print("Error: Please enter valid numeric values.")

# Executes if no exception occurs
else:
    print("Division performed successfully.")

# Executes always
finally:
    print("Program finished.")
