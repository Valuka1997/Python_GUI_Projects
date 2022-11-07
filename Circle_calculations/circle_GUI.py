import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

def calcu():
    {
        print("done")

    }

root = tk.Tk()
#setting title
root.title("Circle Properties Calculator")
#setting window size
width=350
height=350
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

topic=tk.Label(root)
ft = tkFont.Font(family='Times',size=18)
topic["font"] = ft
topic["fg"] = "#333333"
topic["justify"] = "center"
topic["text"] = "Circle Properties Calculator"
topic.place(x=30,y=20,width=293,height=33)

radius_lbl=tk.Label(root)
ft = tkFont.Font(family='Times',size=12)
radius_lbl["font"] = ft
radius_lbl["fg"] = "#333333"
radius_lbl["justify"] = "left"
radius_lbl["text"] = "Radius"
radius_lbl.place(x=10,y=90,width=90,height=25)

diameter_lbl=tk.Label(root)
ft = tkFont.Font(family='Times',size=12)
diameter_lbl["font"] = ft
diameter_lbl["fg"] = "#333333"
diameter_lbl["justify"] = "left"
diameter_lbl["text"] = "Diameter"
diameter_lbl.place(x=10,y=140,width=90,height=25)

circumference_lbl=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
circumference_lbl["font"] = ft
circumference_lbl["fg"] = "#333333"
circumference_lbl["justify"] = "left"
circumference_lbl["text"] = "Circumference"
circumference_lbl.place(x=10,y=190,width=90,height=25)


area_lbl=tk.Label(root)
ft = tkFont.Font(family='Times',size=12)
area_lbl["font"] = ft
area_lbl["fg"] = "#333333"
area_lbl["justify"] = "left"
area_lbl["text"] = "Area"
area_lbl.place(x=10,y=240,width=90,height=25)

radius_entry=tk.Entry(root)
radius_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
radius_entry["font"] = ft
radius_entry["fg"] = "#333333"
radius_entry["justify"] = "center"
radius_entry["text"] = ""
radius_entry.place(x=110,y=90,width=210,height=30)

diameter_entry=tk.Entry(root)
diameter_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
diameter_entry["font"] = ft
diameter_entry["fg"] = "#333333"
diameter_entry["justify"] = "center"
diameter_entry["text"] = ""
diameter_entry.place(x=110,y=140,width=210,height=30)

circumference_entry=tk.Entry(root)
circumference_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
circumference_entry["font"] = ft
circumference_entry["fg"] = "#333333"
circumference_entry["justify"] = "center"
circumference_entry["text"] = ""
circumference_entry.place(x=110,y=190,width=210,height=30)

area_entry=tk.Entry(root)
area_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
area_entry["font"] = ft
area_entry["fg"] = "#333333"
area_entry["justify"] = "center"
area_entry["text"] = ""
area_entry.place(x=110,y=240,width=210,height=30)

btn = Button(root, command=calcu)
btn["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times', size=10)
btn["font"] = ft
btn["fg"] = "#000000"
btn["justify"] = "center"
btn["text"] = "Calculate"
# btn['state'] = "disabled"
btn.place(x=100, y=280, width=190, height=55)

root.mainloop()
