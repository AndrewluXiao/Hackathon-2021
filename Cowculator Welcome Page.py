from tkinter import *
from tkinter import ttk

def first_page():
    first_page = Tk()
    first_page.title("Cowculator")
    first_page.geometry('500x500')

    welcome_sign = Label(first_page, text = "Welcome to Cowculator!")
    welcome_sign.place(relx=.5,rely=.2,anchor = CENTER)


 
    # set Button grid

    btn =Button(first_page, text = 'Enter',fg='green', command = lambda: [first_page.destroy(),second_page()])
    btn.place(relx=0.5,rely=0.5, anchor = CENTER)
    first_page.mainloop()

def second_page():
    
    page2 = Tk()
    page2.title("About Cowculator")
    page2.geometry('500x500')

    lbl = Label(page2, text = "Why does this matter?")
    lbl.place(relx=.5,rely=.2,anchor = CENTER)

    about = Label(page2, text="This is important because...")
    about.place(relx=.5,rely=.3, anchor = CENTER)




    calculate_footprint = Button(page2, text = "Calculate your footprint" ,
                 fg = "green", command = lambda:[page2.destroy(), third_page()])
    calculate_footprint.place(relx=0.5,rely=0.5, anchor = CENTER)

  
def third_page():
    page3 = Tk()
    page3.title("Calculating...")
    page3.geometry('500x500')


    ask_acreage= Label(page3, text = "Input your farm's acreage")
    ask_acreage.place(relx=.5,rely=.2,anchor = CENTER)



    
    #Access the Menu Widget using StringVar function
    access= StringVar()
    #Create an instance of Menu in the frame
    main_menu = OptionMenu(page3, access, "500-1000", "1001-", "Python", "Rust","Go","Ruby")
    main_menu.pack()

    
    input_acreage = Entry(page3, width=10)
    input_acreate.place(relx=.5, rely=.35,anchor = CENTER)

  

    def clicked():
        res = "You have a total of" + txt.get() + "acres."
        ask_acreage.configure(text = res)

    btn3 = Button(page3, text="Calculate", fg="green", command=clicked())
    btn3.place(relx=0.5,rely=0.5, anchor = CENTER)

    btn4 = Button(page3, text = "Which animal?" ,
                 fg = "red", command = lambda:[root3.destroy()])
    btn4.place(relx=0.5,rely=0.5, anchor = CENTER)
    

def main():
    first_page()

main()

