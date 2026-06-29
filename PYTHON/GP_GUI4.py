from tkinter import*
from tkinter import messagebox
top=Tk()
top.title("Button Pageee!!!")
top.geometry("1000x1000")

def fun():
    messagebox.showinfo("Hello","Red has been clicked.")

btn1=Button(top,text="Red",bg="Red",fg="Black",width=10,height=5,command=fun())
btn1.pack(side="left")
btn2=Button(top,text="Blue",bg="Blue",fg="Orange",width=5,height=5,command=fun())
btn2.pack(side="top")
btn3=Button(top,text="Green",bg="Green",fg="purple",activebackground="Yellow",height=5,width=5,command=fun())
btn3.pack(side="bottom")
top.mainloop()