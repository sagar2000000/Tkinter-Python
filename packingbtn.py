from tkinter import *


root = Tk()
root.geometry("543x433")
def hello():
 print("Hello btn")
frame =Frame(root,borderwidth=6,bg="red",relief=SUNKEN)

frame.pack(side=LEFT,anchor="nw")

b1=Button(frame,fg="blue",text="Click here",command=hello)
b1.pack(side=RIGHT)
b2=Button(frame,fg="blue",text="Click hereee",command=hello)
b2.pack(side=RIGHT,padx=12)
b3=Button(frame,fg="blue",text="Click hereeeeeee")
b3.pack(side=RIGHT,padx=23)
root.mainloop()