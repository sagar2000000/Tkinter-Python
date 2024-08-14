from tkinter import *

root = Tk()
root.geometry("543x453")



def getVals():
  print("Submitting Form")
  print(f"{nameval.get(), phoneval.get(), genderval.get(), emergencyval.get(), paymentmodeval.get(), foodserviceval.get()}")
  with open("records.txt","a") as f:
    f.write(f"{nameval.get(), phoneval.get(), genderval.get(), emergencyval.get(), paymentmodeval.get(), foodserviceval.get()} \n")

root.title("Form")
Label(root,text="Welcome to Tkinter Learnings",font="comicsansms 13 bold",pady=5).grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency Contact")
paymentmode = Label(root,text="Payment Mode")


name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

nameval = StringVar()
phoneval = StringVar()
genderval = StringVar()
emergencyval = StringVar()
paymentmodeval = StringVar()
foodserviceval = IntVar()

nameentry=Entry(root,textvariable=nameval)
phoneentry=Entry(root,textvariable=phoneval)
genderentry=Entry(root,textvariable=genderval)
emergencyentry=Entry(root,textvariable=emergencyval)
paymentmodeentry=Entry(root,textvariable=paymentmodeval)


nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

foodservice = Checkbutton(text="Want to prebook your meals?",variable=foodserviceval)
foodservice.grid(row=6,column=3)

Button(text="Submit",command=getVals).grid(row=7,column=3)

root.mainloop()