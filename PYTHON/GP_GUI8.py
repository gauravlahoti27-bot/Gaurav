import tkinter as tk
from tkinter import ttk

def submit():
    name = name_entry.get()
    branch = branch_combo.get()
    game = game_entry.get()

    output_label.config(
        text=f"Name: {name}\nBranch: {branch}\nFavorite Game: {game}"
    )

root = tk.Tk()
root.title("College Admission Form")
root.geometry("350x300")

title = tk.Label(root, text="College Admission Registration", font=("Arial",14))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

name_label = tk.Label(frame, text="Name")
name_label.grid(row=0, column=0, padx=10, pady=5)

name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

branch_label = tk.Label(frame, text="Branch")
branch_label.grid(row=1, column=0, padx=10, pady=5)

branch_combo = ttk.Combobox(frame)
branch_combo['values'] = ("Computer", "Mechanical", "Civil", "Electrical", "IT","AIDS")
branch_combo.grid(row=1, column=1, padx=10, pady=5)

game_label = tk.Label(frame, text="Favorite Game")
game_label.grid(row=2, column=0, padx=10, pady=5)

game_entry = tk.Entry(frame)
game_entry.grid(row=2, column=1, padx=10, pady=5)

submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial",12))
output_label.pack(pady=10)

root.mainloop()
