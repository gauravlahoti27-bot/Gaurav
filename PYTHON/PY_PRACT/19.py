from tkinter import*
root = Tk()
def Onclick():
    print("Button Clicked")

root.title("Button Click Example")
btn = Button(root,text="Click",command=Onclick)
btn.pack()
label = Label(root,text="Hello World")
label.pack()
root.mainloop()