import tkinter as tk
from tkinter import ttk

def convert():
    value = float(entry.get())
    conversion = combo.get()

    if conversion == "Rupees to Dollars":
        result = value / 83   
        output.config(text=f"{result:.2f} USD")

    elif conversion == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
        output.config(text=f"{result:.2f} °F")

    elif conversion == "Inches to Feet":
        result = value / 12
        output.config(text=f"{result:.2f} ft")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("350x250")

title = tk.Label(root, text="Unit Converter", font=("Arial",16))
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial",12))
entry.pack(pady=10)

combo = ttk.Combobox(root)
combo['values'] = ("Rupees to Dollars",
                   "Celsius to Fahrenheit",
                   "Inches to Feet")
combo.current(0)
combo.pack(pady=10)

btn = tk.Button(root, text="Convert", command=convert)
btn.pack(pady=10)

output = tk.Label(root, text="Result will appear here", font=("Arial",12))
output.pack(pady=10)
root.mainloop()
