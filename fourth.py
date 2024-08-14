from tkinter import *

root=Tk()

root.geometry("633x444")
f1= Frame(root,bg="red",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
f2= Frame(root,borderwidth=9,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill="x")
l =Label(f1,text="Project Tkinter")
l.pack(pady=41)
l2 =Label(f2,text="Project SAGAR",font="bold",fg="blue")
l2.pack(pady=4)

root.mainloop()     