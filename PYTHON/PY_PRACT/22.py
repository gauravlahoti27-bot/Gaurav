from tkinter import *

def submit():
    name = name_entry.get()
    branch = branch_var.get()
    games = [game for game, var in game_vars.items() if var.get()]

    if games:
        game_text = " and enjoys playing " + ", ".join(games)
    else:
        game_text = ""

    result.set(f"Your name is {name}. {name} is from {branch} Department{game_text}.")

# Create window
root = Tk()
root.title("College Admission Form")
root.geometry("500x400")

# Name
Label(root, text="Enter student name:").grid(row=0, column=0, sticky="w", padx=20, pady=5)
name_entry = Entry(root, width=25)
name_entry.grid(row=0, column=1, columnspan=2, pady=5, padx=20)

# Branch
Label(root, text="Select your branch").grid(row=1, column=0, sticky="w", padx=20, pady=(20, 5))
branch_var = StringVar(value="Computer Engineering")

branches = ["Computer Engineering", "Information Technology", "Artificial Intelligence and Data Science"]

for i, branch in enumerate(branches):
    Radiobutton(root, text=branch, variable=branch_var, value=branch).grid(row=1+i, column=1, sticky="w", padx=10)

# Games
Label(root, text="Select your favorite game").grid(row=4, column=0, sticky="w", padx=20, pady=(20, 5))

game_vars = {game: IntVar() for game in ["Cricket", "Football", "Badminton", "Swimming"]}

for i, game in enumerate(game_vars):
    Checkbutton(root, text=game, variable=game_vars[game]).grid(row=4+i, column=1, sticky="w", padx=20)

# Submit Button
Button(root, text="Submit", command=submit, width=12).grid(row=8, column=1, pady=20)

# Result Label
result = StringVar()
Label(root, textvariable=result, padx=20, pady=15).grid(row=9, column=0, columnspan=3)

root.mainloop()