from tkinter import *
from tkinter import ttk
from tkinter import simpledialog

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

   

    acre_lbl = Label(page3, text = "How many acres?")
    acre_lbl.place(relx=.5,rely=.1,anchor = CENTER)
    
    acre_answer = Entry(page3, width=10)
    acre_answer.place(relx=.5,rely=.2,anchor = CENTER)

    def acres_clicked():
    #res = "You have " + acre_answer.get() + "acres."
    #lbl.configure(text = res)
        acre = acre_answer.get()

        
    acre_btn = Button(page3, text = "acres" ,fg = "red", command=acres_clicked)
    acre_btn.place(relx=0.5,rely=0.3, anchor = CENTER)

    

    animal_lbl = Label(page3, text = "What type of animal?")
    animal_lbl.place(relx=.5,rely=.4,anchor = CENTER)
    
    #animal_answer = Entry(page3, width=10)
    #animal_answer.place(relx=.5, rely=.5, anchor = CENTER)
    
    #animal_btn = Button(page3, text = "animal type" ,fg = "red", command=animal_clicked)
    #animal_btn.place(relx=0.5,rely=0.6, anchor = CENTER)

    animal_type = StringVar()
    animal_menu = OptionMenu(page3, animal_type, "Goats", "Cattle", "Chickens", "Sheeps","Pigs")
    animal_menu.place(relx=.5, rely=.5, anchor = CENTER)

    
    #def animal_clicked():
    #res = "You chose " + animal_answer.get()
    #lbl.configure(text = res)
        #animal_type = animal_answer.get()

    
    
    animal_num_lbl = Label(page3, text = "How many?")
    animal_num_lbl.place(relx=.5,rely=.7,anchor = CENTER)
    
    animal_num = Entry(page3, width=10)
    animal_num.place(relx=.5,rely=.8,anchor = CENTER)

    def animal_num_clicked():
    #res = "You have " + animal_num.get() +animal_answer.get()
    #lbl.configure(text = res)
        animal_number = animal_num.get()  


    animal_num_btn = Button(page3, text = "animal number" , fg = "red", command=animal_num_clicked)
    animal_num_btn.place(relx=0.5,rely=0.85, anchor = CENTER)
    

    final_results = Button(page3, text = "Your Results" ,
                 fg = "green", command = lambda:[page3.destroy(), fourth_page()])
    final_results.place(relx=0.5,rely=.95 , anchor = CENTER)


def fourth_page():
    page4 = Tk()
    page4.title("Your farm's carbon footprint")
    page4.geometry('500x500')


    score = Label(page4, text = "Calculated Carbon Footprint:")
    score.grid(row=2, column=10)
    
    #Score (compared to our farm data)
    CO2 = Label(page4, text = "CO2:")
    CO2.grid(row=4, column=10)

    NO2 = Label(page4, text = "NO2:")
    NO2.grid(row=6, column=10)

    CH4 = Label(page4, text = "CH4:")
    CH4.grid(row=8, column=10)


    #Blurb about how to improve based on which category is the worst
    rec = Label (page4, text = 'Based on your calculated footprint, we recommend... ')
    rec.grid(row=10, column=10)

    
    #Redo button



def main():
    acre = 0
    animal_type = ''
    animal_number = 0
  

    answer = 0
    first_page()

main()

