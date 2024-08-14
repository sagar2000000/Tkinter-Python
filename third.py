from tkinter import *

root =Tk()

root.geometry("904x543")
root.title("Sagar GUI")
title_label=Label(text="Captain Jack Sparrow is a fictional character and the main protagonist \nof the Pirates of the \nCaribbean film series and franchise. An early iteration of Sparrow was\n created by screenwriters Ted Elliott and Terry Rossio, but the final version of the character was created by actor Johnny Depp, who also portrayed him.",bg="red",fg="white",padx=23,pady=40,font=("bold",9),relief=SUNKEN)

# side =top,bottom,left.right
# anchor=nw
title_label.pack(side=BOTTOM,anchor='nw')



root.mainloop()







# text -adds Text
# bd-background
# fg-foreground
# font-sets the font
# padx
# pady
# relief

