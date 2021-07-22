from tkinter import *

window=Tk()

file=open("samp_GUI.txt","a+")

def add():
    file.write(user_value.get() +"\n")
    entry.delete(0,END)
    #entry.insert(0,"a default val")

def save():
    global file
    file.close()
    file=open("samp_GUI.txt","a+")

def close():
    file.close()
    window.destroy()


user_value=StringVar()
entry=Entry(window,textvariable=user_value)
entry.grid(row=0,column=0)

b1=Button(window,text="ADD line",command=add)
b1.grid(row=0,column=1)

b2=Button(window,text="SAVE",command=save)
b2.grid(row=0,column=2)

b3=Button(window,text="save and close",command=close)
b3.grid(row=0,column=3)

window.mainloop()

