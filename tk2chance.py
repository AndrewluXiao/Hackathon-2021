from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Hello World")
root.geometry('200x200')

lbl = Label(root, text = "type something")
lbl.place(relx=.5,rely=.2,anchor = CENTER)


txt = Entry(root, width=10)
txt.place(relx=.5, rely=.35,anchor = CENTER)

def clicked():
    res = "You wrote " + txt.get()
    lbl.configure(text = res)


btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# set Button grid
btn.place(relx=0.5,rely=0.5, anchor = CENTER)

btn2 = Button(root, text = 'exit',fg ="green",command = root.destroy)
btn2.grid(column = 8, row = 3)
btn2.place(relx=.5,rely=.65, anchor = CENTER)


root.mainloop()
