# ------------------------------------------------------------
# Q1. Area of Circle, Rectangle and Triangle
# ------------------------------------------------------------
import math

print("=== Q1: Area Calculator ===")

# Circle
r = float(input("Enter radius of circle: "))
area_circle = math.pi * r * r
print(f"Area of Circle = {area_circle:.2f}")

# Rectangle
l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
area_rect = l * b
print(f"Area of Rectangle = {area_rect:.2f}")

# Triangle
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
area_tri = 0.5 * base * height
print(f"Area of Triangle = {area_tri:.2f}")


# ------------------------------------------------------------
# Q2. Multiply all Numbers in a List
# ------------------------------------------------------------
print("\n=== Q2: Product of List Elements ===")

def multiply_list(lst):
    product = 1
    for num in lst:
        product = product * num
    return product

numbers = [2, 3, 4, 5]
result = multiply_list(numbers)
print(f"List : {numbers}")
print(f"Product of all elements = {result}")


# ------------------------------------------------------------
# Q3. Leap Year Check
# ------------------------------------------------------------
print("\n=== Q3: Leap Year Check ===")

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")


# ------------------------------------------------------------
# Q4. HCF / GCD of Two Numbers
# ------------------------------------------------------------
print("\n=== Q4: HCF / GCD ===")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Using Euclidean algorithm
x, y = a, b
while y != 0:
    x, y = y, x % y

print(f"HCF of {a} and {b} = {x}")


# ------------------------------------------------------------
# Q5. Sort Words Alphabetically & Count Vowels/Consonants
# ------------------------------------------------------------
print("\n=== Q5: Word Sort and Vowel/Consonant Count ===")

sentence = input("Enter a string: ")

# Sort words alphabetically
words = sentence.split()
words.sort()
print("Words in alphabetical order:", " ".join(words))

# Count vowels and consonants
vowels = 0
consonants = 0
for ch in sentence:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(f"Total Vowels     = {vowels}")
print(f"Total Consonants = {consonants}")


# ------------------------------------------------------------
# Q6. Transpose a Matrix
# ------------------------------------------------------------
print("\n=== Q6: Matrix Transpose ===")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

# Create empty transpose matrix
transpose = []
for i in range(cols):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)

print("Original Matrix:")
for row in matrix:
    print(row)

print("Transposed Matrix:")
for row in transpose:
    print(row)


# ------------------------------------------------------------
# Q7. Palindrome Check
# ------------------------------------------------------------
print("\n=== Q7: Palindrome Check ===")

string = input("Enter a string: ")
reversed_string = string[::-1]

if string.lower() == reversed_string.lower():
    print(f"'{string}' is a Palindrome")
else:
    print(f"'{string}' is NOT a Palindrome")


# ------------------------------------------------------------
# Q8. Matrix Multiplication
# ------------------------------------------------------------
print("\n=== Q8: Matrix Multiplication ===")

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])

# Check if multiplication is possible
if cols_A != rows_B:
    print("Matrix multiplication NOT possible!")
    print(f"Columns of A ({cols_A}) must equal Rows of B ({rows_B})")
else:
    print("Matrix multiplication is possible.")

    # Create result matrix filled with zeros
    result = []
    for i in range(rows_A):
        result.append([0] * cols_B)

    # Multiply
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    print("Matrix A:", A)
    print("Matrix B:", B)
    print("Result (A x B):")
    for row in result:
        print(row)


# ------------------------------------------------------------
# Q9. Calculator Class
# ------------------------------------------------------------
print("\n=== Q9: Calculator Class ===")

class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Cannot divide by zero!"
        return a / b

# Create object and demonstrate
calc = Calculator()
print("Addition       : 10 + 5 =", calc.addition(10, 5))
print("Subtraction    : 10 - 5 =", calc.subtraction(10, 5))
print("Multiplication : 10 * 5 =", calc.multiplication(10, 5))
print("Division       : 10 / 5 =", calc.division(10, 5))


# ============================================================
#  UNIT 2 — OBJECT-ORIENTED PROGRAMMING
# ============================================================

# ------------------------------------------------------------
# Q10. Class Variable — College Name
# ------------------------------------------------------------
print("\n=== Q10: Class Variable ===")

class Student:
    college_name = "Mumbai University"   # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    def display(self):
        print(f"Student: {self.name}, College: {Student.college_name}")

s1 = Student("Rahul")
s2 = Student("Priya")

s1.display()
s2.display()

# Change class variable using one instance
s1.change_college("IIT Bombay")
print("After changing college name using s1:")
s1.display()
s2.display()   # Change reflected in s2 as well


# ------------------------------------------------------------
# Q11. Static Method — Count Instances
# ------------------------------------------------------------
print("\n=== Q11: Static Method to Count Instances ===")

class Counter:
    count = 0   # static / class variable

    def __init__(self):
        Counter.count += 1

    @staticmethod
    def show_count():
        print(f"Total instances created = {Counter.count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
Counter.show_count()


# ------------------------------------------------------------
# Q12. Nested Class — Person and DOB
# ------------------------------------------------------------
print("\n=== Q12: Nested Class (Person and DOB) ===")

class Person:
    def __init__(self, person_name):
        self.person_name = person_name

    def display(self):
        print(f"Person Name: {self.person_name}")

    class DOB:
        def __init__(self, day, month, year):
            self.date_of_birth = f"{day:02d}/{month:02d}/{year}"

        def display(self):
            print(f"Date of Birth: {self.date_of_birth}")

p = Person("Amit Sharma")
p.display()

dob = Person.DOB(15, 8, 2005)
dob.display()


# ------------------------------------------------------------
# Q13. super() — Call Parent Class Constructor
# ------------------------------------------------------------
print("\n=== Q13: Using super() ===")

class Father:
    def __init__(self):
        self.property = "House and Land"

    def display(self):
        print(f"Father's property: {self.property}")

class Son(Father):
    def __init__(self):
        super().__init__()   # calls Father's constructor
        self.own_property = "Car"

    def display(self):
        super().display()    # calls Father's display
        print(f"Son's own property: {self.own_property}")

son = Son()
son.display()


# ------------------------------------------------------------
# Q14. Inheritance — Square and Rectangle
# ------------------------------------------------------------
print("\n=== Q14: Base Class Constructor via Derived Class ===")

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Area of Rectangle = {self.length * self.breadth}")

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # a square has equal length and breadth
        self.side = side

    def area(self):
        print(f"Area of Square = {self.side * self.side}")

r = Rectangle(5, 3)
r.area()

s = Square(4)
s.area()


# ============================================================
#  UNIT 3 — REGULAR EXPRESSIONS
# ============================================================
import re

# ------------------------------------------------------------
# Q15. Strings Starting with 'p' and Exactly 4 Characters
# ------------------------------------------------------------
print("\n=== Q15: Words starting with 'p', length 4 ===")

words = ["pink", "pen", "play", "park", "pune", "py", "python", "pear"]
pattern = r'\bp\w{3}\b'   # p + exactly 3 more chars = 4 total

for word in words:
    if re.fullmatch(r'p\w{3}', word):
        print(word)


# ------------------------------------------------------------
# Q16. Replace Substring using Regex
# ------------------------------------------------------------
print("\n=== Q16: Replace Substring ===")

text = input("Enter a string: ")
old = input("Enter word to replace: ")
new = input("Enter new word: ")

result = re.sub(old, new, text)
print(f"Result: {result}")


# ------------------------------------------------------------
# Q17. Words Starting with 'm'
# ------------------------------------------------------------
print("\n=== Q17: Words starting with 'm' ===")

sentence = "mango is a sweet fruit and muskmelon is also sweet and monkey likes mango"
matches = re.findall(r'\bm\w*', sentence)
print("Words starting with 'm':", matches)


# ------------------------------------------------------------
# Q18. Words with Exactly 5 Characters
# ------------------------------------------------------------
print("\n=== Q18: Words with exactly 5 characters ===")

sentence = "apple mango is sweet fruit grape"
matches = re.findall(r'\b\w{5}\b', sentence)
print("Words with exactly 5 characters:", matches)


# ------------------------------------------------------------
# Q19. Words with at Least 4 Characters
# ------------------------------------------------------------
print("\n=== Q19: Words with at least 4 characters ===")

sentence = "I love Python programming it is fun"
matches = re.findall(r'\b\w{4,}\b', sentence)
print("Words with at least 4 characters:", matches)


# ------------------------------------------------------------
# Q20. Last Word if it Starts with 't'
# ------------------------------------------------------------
print("\n=== Q20: Last word starting with 't' ===")

sentence = "She went to the market"
match = re.search(r'\bt\w+$', sentence)

if match:
    print(f"Last word starting with 't': {match.group()}")
else:
    print("Last word does NOT start with 't'")


# ------------------------------------------------------------
# Q21. Extract Phone Number from Text
# ------------------------------------------------------------
# Assumption: 10-digit Indian mobile number (may start with +91 or 0)
print("\n=== Q21: Extract Phone Number ===")

text = "Please contact Rohit at +91-9876543210 or at 022-27654321"
pattern = r'(\+91[-\s]?)?[6-9]\d{9}'  # Indian mobile: starts with 6-9, 10 digits

matches = re.findall(pattern, text)
all_matches = re.findall(r'(\+91[-\s]?[6-9]\d{9}|[6-9]\d{9})', text)
print("Phone numbers found:", all_matches)


# ------------------------------------------------------------
# Q22. Words Starting with 'ak' or 'ab'
# ------------------------------------------------------------
print("\n=== Q22: Words starting with 'ak' or 'ab' ===")

sentence = "akash and abhishek went to akola with abhinav"
matches = re.findall(r'\b(ak|ab)\w*', sentence)
print("Words starting with 'ak' or 'ab':", matches)


# ------------------------------------------------------------
# Q23. Extract Date of Birth (dd/mm/yyyy or dd-mm-yyyy)
# ------------------------------------------------------------
print("\n=== Q23: Extract Date of Birth ===")

text = "My name is Sneha and my date of birth is 14/08/2003 as per records."
pattern = r'\b\d{2}[/\-]\d{2}[/\-]\d{4}\b'

match = re.search(pattern, text)
if match:
    print(f"Date of Birth found: {match.group()}")
else:
    print("No date found in the string.")


# ------------------------------------------------------------
# Q24. String Starts with 'He'
# ------------------------------------------------------------
print("\n=== Q24: String starts with 'He' ===")

string = "Hello, welcome to Python!"
if re.match(r'He', string):
    print(f"'{string}' starts with 'He'")
else:
    print(f"'{string}' does NOT start with 'He'")


# ------------------------------------------------------------
# Q25. Search for a Word at the End of a String
# ------------------------------------------------------------
print("\n=== Q25: Search for word at end of string ===")

sentence = "I love programming in Python"
word = "Python"

pattern = r'\b' + word + r'\b$'
if re.search(pattern, sentence):
    print(f"'{word}' found at the end of the string.")
else:
    print(f"'{word}' NOT found at the end.")


# ------------------------------------------------------------
# Q26. Retrieve Names and Marks from a String
# ------------------------------------------------------------
print("\n=== Q26: Extract Names and Marks ===")

text = "Vijay got 56 marks, Sonal got 98 marks, Rahul got 45 marks, Priya got 88 marks"

# Names start with a capital letter; marks are digits
matches = re.findall(r'([A-Z][a-z]+) got (\d+) marks', text)

print(f"{'Name':<10} {'Marks'}")
print("-" * 20)
for name, marks in matches:
    print(f"{name:<10} {marks}")


# ============================================================
#  UNIT 4 — NUMPY
# ============================================================
import numpy as np

# ------------------------------------------------------------
# Q27. 1D, 2D, 3D Arrays — Reshape, Slice, Index
# ------------------------------------------------------------
print("\n=== Q27: NumPy 1D, 2D, 3D Arrays ===")

# 1D Array
arr1d = np.array([1, 2, 3, 4, 5, 6])
print("1D Array:", arr1d)
print("Element at index 2:", arr1d[2])
print("Slice [1:4]:", arr1d[1:4])

# Reshape 1D to 2D
arr2d = arr1d.reshape(2, 3)
print("\n2D Array (reshaped from 1D):\n", arr2d)
print("Element at row 1, col 2:", arr2d[1][2])
print("First row:", arr2d[0])

# 3D Array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:\n", arr3d)
print("Element [0][1][1]:", arr3d[0][1][1])


# ------------------------------------------------------------
# Q28. Element-wise Operations on Two Arrays
# ------------------------------------------------------------
print("\n=== Q28: Element-wise Operations ===")

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])

print("Array A:", a)
print("Array B:", b)
print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)


# ------------------------------------------------------------
# Q29. String-type NumPy Array
# ------------------------------------------------------------
print("\n=== Q29: String-type NumPy Array ===")

str_array = np.array(["Mumbai", "Pune", "Nashik", "Nagpur"], dtype=str)
print("String Array:", str_array)
print("Data type:", str_array.dtype)
print("First element:", str_array[0])


# ------------------------------------------------------------
# Q30. Copy a NumPy Array
# ------------------------------------------------------------
print("\n=== Q30: Copy NumPy Array ===")

original = np.array([5, 10, 15, 20, 25])
copy = original.copy()

print("Original:", original)
print("Copy    :", copy)
print("Are they identical?", np.array_equal(original, copy))

# Show that modifying copy doesn't affect original
copy[0] = 99
print("\nAfter modifying copy[0] to 99:")
print("Original:", original)
print("Copy    :", copy)


# ------------------------------------------------------------
# Q31. Display Elements of 2D Array using Indexing
# ------------------------------------------------------------
print("\n=== Q31: 2D Array Indexing ===")

matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

print("2D Array:\n", matrix)
print("\nElement at [0][0]:", matrix[0][0])
print("Element at [1][2]:", matrix[1][2])
print("Second row       :", matrix[1])
print("Third column     :", matrix[:, 2])


# ------------------------------------------------------------
# Q32. Array of Even Numbers from 2 to 50
# ------------------------------------------------------------
print("\n=== Q32: Even Numbers 2 to 50 ===")

even_array = np.arange(2, 51, 2)
print("Even numbers from 2 to 50:")
print(even_array)


# ============================================================
#  UNIT 5 — PANDAS & DATA VISUALIZATION
# ============================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# Q33. Iris Dataset Analysis
# ------------------------------------------------------------
print("\n=== Q33: Iris Dataset Analysis ===")

# Load Iris dataset
from sklearn.datasets import load_iris

iris_data = load_iris()
df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

# i. First 8 rows
print("i) First 8 rows:")
print(df.head(8))

# ii. Column names
print("\nii) Column names:")
print(df.columns.tolist())

# iii. Fill missing values with column mean
df_filled = df.copy()
numeric_cols = df_filled.select_dtypes(include='number').columns
df_filled[numeric_cols] = df_filled[numeric_cols].fillna(df_filled[numeric_cols].mean())
print("\niii) Missing values filled with mean (no missing values in Iris, but code is ready).")

# iv. Remove rows with missing values
df_dropped = df.dropna()
print(f"iv) Rows after dropping NaN: {len(df_dropped)}")

# v. Group by species
grouped = df.groupby('species')
print("\nv) Groups (species):")
for name, group in grouped:
    print(f"   Species: {name}, Count: {len(group)}")

# vi. Mean, Min, Max of Sepal Length
sepal_col = 'sepal length (cm)'
print(f"\nvi) Sepal Length Statistics:")
print(f"    Mean = {df[sepal_col].mean():.2f}")
print(f"    Min  = {df[sepal_col].min():.2f}")
print(f"    Max  = {df[sepal_col].max():.2f}")


# ------------------------------------------------------------
# Q34. Toyota Corolla Dataset Analysis
# ------------------------------------------------------------
print("\n=== Q34: Toyota Corolla Dataset ===")
print("NOTE: Download the dataset from Kaggle and update the path below.")

# Load dataset (update path as needed)
# df_car = pd.read_csv("ToyotaCorolla.csv")

# Showing code structure with a sample dataset for demonstration
df_car = pd.DataFrame({
    'Age':   [2, 3, 5, 7, 8, 10, 12, 15, 1, 4],
    'Price': [15000, 13000, 10000, 8000, 7500, 5000, 4000, 3000, 18000, 11000],
    'KM':    [20000, 35000, 60000, 80000, 90000, 120000, 150000, 180000, 10000, 45000],
    'FuelType': ['Petrol', 'Diesel', 'Petrol', 'CNG', 'Diesel', 'Petrol', 'CNG', 'Diesel', 'Petrol', 'Diesel']
})

# i. Scatter plot: Age vs Price
plt.figure(figsize=(6, 4))
plt.scatter(df_car['Age'], df_car['Price'], color='blue')
plt.xlabel("Age of Car (years)")
plt.ylabel("Price")
plt.title("Age vs Price of Cars")
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/q34_scatter.png")
plt.show()
print("i) Scatter plot saved.")

# ii. Histogram: KM driven
plt.figure(figsize=(6, 4))
plt.hist(df_car['KM'], bins=5, color='green', edgecolor='black')
plt.xlabel("Kilometers Driven")
plt.ylabel("Frequency")
plt.title("Histogram of KM Driven")
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/q34_histogram.png")
plt.show()
print("ii) Histogram saved.")

# iii. Bar plot: Fuel Type distribution
fuel_counts = df_car['FuelType'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(fuel_counts.index, fuel_counts.values, color=['blue', 'orange', 'green'])
plt.xlabel("Fuel Type")
plt.ylabel("Count")
plt.title("Distribution of Cars by Fuel Type")
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/q34_barplot.png")
plt.show()
print("iii) Bar plot saved.")

# iv. Pie chart: Fuel Type percentage
plt.figure(figsize=(5, 5))
plt.pie(fuel_counts.values, labels=fuel_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Fuel Type Distribution (%)")
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/q34_piechart.png")
plt.show()
print("iv) Pie chart saved.")

# v. Box plot: Price by Fuel Type
plt.figure(figsize=(6, 4))
df_car.boxplot(column='Price', by='FuelType', grid=False)
plt.xlabel("Fuel Type")
plt.ylabel("Price")
plt.title("Car Price Distribution by Fuel Type")
plt.suptitle("")   # remove auto title
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/q34_boxplot.png")
plt.show()
print("v) Box plot saved.")


# ============================================================
#  UNIT 6 — GUI PROGRAMMING WITH TKINTER
# ============================================================

# NOTE: Tkinter programs open a window and must be run separately.
# Each Q35–Q39 is a complete standalone program.

# ------------------------------------------------------------
# Q35. Conversion Utilities GUI
# ------------------------------------------------------------
"""
# Run this program separately in IDLE / VS Code

import tkinter as tk
from tkinter import ttk

def convert():
    try:
        value = float(entry_value.get())
        choice = combo.get()

        if choice == "Rupees to Dollars":
            result = value / 83
            label_result.config(text=f"Result: {result:.4f} Dollars")

        elif choice == "Dollars to Rupees":
            result = value * 83
            label_result.config(text=f"Result: {result:.2f} Rupees")

        elif choice == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
            label_result.config(text=f"Result: {result:.2f} °F")

        elif choice == "Fahrenheit to Celsius":
            result = (value - 32) * 5/9
            label_result.config(text=f"Result: {result:.2f} °C")

        elif choice == "Inches to Feet":
            result = value / 12
            label_result.config(text=f"Result: {result:.4f} Feet")

        elif choice == "Feet to Inches":
            result = value * 12
            label_result.config(text=f"Result: {result:.2f} Inches")

    except ValueError:
        label_result.config(text="Please enter a valid number!")

# Window setup
root = tk.Tk()
root.title("Conversion Utility")
root.geometry("400x250")

tk.Label(root, text="Conversion Utility", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Enter Value:").pack()
entry_value = tk.Entry(root, width=20)
entry_value.pack(pady=5)

options = ["Rupees to Dollars", "Dollars to Rupees",
           "Celsius to Fahrenheit", "Fahrenheit to Celsius",
           "Inches to Feet", "Feet to Inches"]

combo = ttk.Combobox(root, values=options, width=25)
combo.set("Celsius to Fahrenheit")
combo.pack(pady=5)

tk.Button(root, text="Convert", command=convert, bg="blue", fg="white").pack(pady=8)
label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
label_result.pack()

root.mainloop()
"""

print("\n=== Q35: Conversion Utility GUI ===")
print("Uncomment and run the Q35 code block separately.")


# ------------------------------------------------------------
# Q36. Area Calculator GUI
# ------------------------------------------------------------
"""
# Run this program separately

import tkinter as tk
import math

def calc_area():
    shape = var.get()
    try:
        if shape == "Circle":
            r = float(entry1.get())
            area = math.pi * r * r
            label_result.config(text=f"Area of Circle = {area:.2f}")

        elif shape == "Rectangle":
            l = float(entry1.get())
            b = float(entry2.get())
            area = l * b
            label_result.config(text=f"Area of Rectangle = {area:.2f}")

        elif shape == "Triangle":
            base = float(entry1.get())
            height = float(entry2.get())
            area = 0.5 * base * height
            label_result.config(text=f"Area of Triangle = {area:.2f}")

    except ValueError:
        label_result.config(text="Enter valid numbers!")

def update_labels(*args):
    shape = var.get()
    if shape == "Circle":
        label1.config(text="Radius:")
        label2.config(text="")
        entry2.config(state="disabled")
    else:
        label1.config(text="Length / Base:")
        label2.config(text="Breadth / Height:")
        entry2.config(state="normal")

root = tk.Tk()
root.title("Area Calculator")
root.geometry("380x280")

tk.Label(root, text="Area Calculator", font=("Arial", 14, "bold")).pack(pady=10)

var = tk.StringVar(value="Circle")
var.trace("w", update_labels)
frame_radio = tk.Frame(root)
frame_radio.pack()
for shape in ["Circle", "Rectangle", "Triangle"]:
    tk.Radiobutton(frame_radio, text=shape, variable=var, value=shape).pack(side="left", padx=10)

frame = tk.Frame(root)
frame.pack(pady=10)

label1 = tk.Label(frame, text="Radius:", width=18, anchor="w")
label1.grid(row=0, column=0)
entry1 = tk.Entry(frame, width=15)
entry1.grid(row=0, column=1, pady=4)

label2 = tk.Label(frame, text="", width=18, anchor="w")
label2.grid(row=1, column=0)
entry2 = tk.Entry(frame, width=15, state="disabled")
entry2.grid(row=1, column=1, pady=4)

tk.Button(root, text="Calculate Area", command=calc_area, bg="green", fg="white").pack(pady=8)
label_result = tk.Label(root, text="Area = ", font=("Arial", 12))
label_result.pack()

root.mainloop()
"""

print("\n=== Q36: Area Calculator GUI ===")
print("Uncomment and run the Q36 code block separately.")


# ------------------------------------------------------------
# Q37. College Admission Registration Form GUI
# ------------------------------------------------------------
"""
# Run this program separately

import tkinter as tk

def submit():
    name   = entry_name.get()
    branch = var_branch.get()
    game   = entry_game.get()

    output = (f"--- Admission Details ---\n"
              f"Name   : {name}\n"
              f"Branch : {branch}\n"
              f"Game   : {game}")
    label_output.config(text=output)

root = tk.Tk()
root.title("College Admission Form")
root.geometry("420x320")

tk.Label(root, text="College Admission Form", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Full Name:", width=15, anchor="w").grid(row=0, column=0, pady=5)
entry_name = tk.Entry(frame, width=25)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Branch:", width=15, anchor="w").grid(row=1, column=0, pady=5)
var_branch = tk.StringVar(value="AIDS")
branches = ["AIDS", "Computer", "IT", "EXTC", "Mechanical"]
from tkinter import ttk
combo_branch = ttk.Combobox(frame, textvariable=var_branch, values=branches, width=22)
combo_branch.grid(row=1, column=1)

tk.Label(frame, text="Favourite Game:", width=15, anchor="w").grid(row=2, column=0, pady=5)
entry_game = tk.Entry(frame, width=25)
entry_game.grid(row=2, column=1)

tk.Button(root, text="Submit", command=submit, bg="blue", fg="white", width=15).pack(pady=10)
label_output = tk.Label(root, text="", font=("Arial", 11), justify="left")
label_output.pack()

root.mainloop()
"""

print("\n=== Q37: College Admission Form GUI ===")
print("Uncomment and run the Q37 code block separately.")


# ------------------------------------------------------------
# Q38. Validate Phone Number and Email ID using Regex
# ------------------------------------------------------------
print("\n=== Q38: Phone Number and Email Validation ===")

import re

phone = input("Enter phone number: ")
email = input("Enter email address: ")

# Phone: 10-digit Indian number, optionally with +91
phone_pattern = r'^(\+91[\-\s]?)?[6-9]\d{9}$'
# Email: standard format user@domain.extension
email_pattern = r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$'

if re.match(phone_pattern, phone):
    print(f"Phone '{phone}' is VALID")
else:
    print(f"Phone '{phone}' is INVALID")

if re.match(email_pattern, email):
    print(f"Email '{email}' is VALID")
else:
    print(f"Email '{email}' is INVALID")


# ------------------------------------------------------------
# Q39. Password Strength Checker using Regex
# ------------------------------------------------------------
print("\n=== Q39: Password Strength Checker ===")

password = input("Enter a password: ")

errors = []

if len(password) < 8:
    errors.append("At least 8 characters required")
if not re.search(r'[A-Z]', password):
    errors.append("At least one UPPERCASE letter required")
if not re.search(r'[a-z]', password):
    errors.append("At least one lowercase letter required")
if not re.search(r'\d', password):
    errors.append("At least one digit required")
if not re.search(r'[!@#$%^&*()_+\-=\[\]{};\':\\|,.<>\/?]', password):
    errors.append("At least one special character required")

if len(errors) == 0:
    print("Password is STRONG ✔")
else:
    print("Password is WEAK ✘")
    print("Reasons:")
    for e in errors:
        print(f"  - {e}")


# ============================================================
#  END OF SOLUTIONS
# ============================================================
print("\n=== All 39 Programs Completed! ===")
