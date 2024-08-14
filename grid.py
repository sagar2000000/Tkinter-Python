from tkinter import *

root=Tk()

root.geometry("543x453")

def getVal():
  print(uservalue.get())
  print(passvalue.get())


user=Label(root,text="Username")
password=Label(root,text="Password")
user.grid()
password.grid(row=1)

# var in tkinter BooleanVar,DoubleVar,Intvar,StringVar
uservalue=StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable=uservalue)
passentry = Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)


btn = Button(text="Submit",command=getVal)
btn.grid()

root.mainloop() 