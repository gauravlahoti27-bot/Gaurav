import tkinter as tk
from tkinter import ttk
import math

def calculate_area():
    shape = shape_combo.get()

    try:
        if shape == "Circle":
            r = float(entry1.get())
            area = math.pi * r * r
            result_label.config(text=f"Area = {area:.2f}")
        elif shape == "Rectangle":
            l = float(entry1.get())
            w = float(entry2.get())
            area = l * w
            result_label.config(text=f"Area = {area:.2f}")
        elif shape == "Triangle":
            b = float(entry1.get())
            h = float(entry2.get())
            area = 0.5 * b * h
            result_label.config(text=f"Area = {area:.2f}")
    except:
        result_label.config(text="Please enter valid numbers")

def update_fields(event):
    shape = shape_combo.get()

    if shape == "Circle":
        label1.config(text="Radius")
        label2.grid_remove()
        entry2.grid_remove()
    elif shape == "Rectangle":
        label1.config(text="Length")
        label2.config(text="Width")
        label2.grid()
        entry2.grid()
    elif shape == "Triangle":
        label1.config(text="Base")
        label2.config(text="Height")
        label2.grid()
        entry2.grid()

root = tk.Tk()
root.title("Area Calculator")
root.geometry("350x300")

title = tk.Label(root, text="Area Calculator", font=("Arial",16))
title.pack(pady=10)

shape_combo = ttk.Combobox(root, values=["Circle","Rectangle","Triangle"])
shape_combo.pack(pady=10)
shape_combo.bind("<<ComboboxSelected>>", update_fields)

frame = tk.Frame(root)
frame.pack(pady=10)

label1 = tk.Label(frame, text="Value 1")
label1.grid(row=0,column=0,padx=5,pady=5)

entry1 = tk.Entry(frame)
entry1.grid(row=0,column=1,padx=5,pady=5)

label2 = tk.Label(frame, text="Value 2")
label2.grid(row=1,column=0,padx=5,pady=5)

entry2 = tk.Entry(frame)
entry2.grid(row=1,column=1,padx=5,pady=5)

calc_button = tk.Button(root,text="Calculate Area",command=calculate_area)
calc_button.pack(pady=10)

result_label = tk.Label(root,text="Area will appear here",font=("Arial",12))
result_label.pack(pady=10)

root.mainloop()
