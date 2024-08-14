from tkinter import *

root =Tk()
root.geometry("1200x1200")
photo=PhotoImage(file="sas.png")
                    
lbl =Label(image=photo)
lbl.pack()
root.mainloop()