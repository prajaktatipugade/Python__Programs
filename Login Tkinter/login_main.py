from tkinter import *

def show_registration_success_page():
    global registration_form
    m.withdraw()  # Hide the registration form window

    registration_success = Tk()
    registration_success.title("Registration Success")
    registration_success.geometry("300x100")

    lnew = Label(registration_success, text="Registration successful!", font=("Times New Roman", 12))
    lnew.pack(pady=20)

    # Create a button to close the success window and exit the application
    close_button = Button(registration_success, text="Close", command=registration_success.destroy)
    close_button.pack()

    registration_success.mainloop()

def register():	
    show_registration_success_page()




m = Tk()
m.geometry("500x500") 
m.title("Registration Form")

l1 = Label(m, text = "Enter Name", width = 10, font=("Times New Roman", 12))
l1.place(x = 20, y = 120)
e1 = Entry(m)
e1.place(x=200, y=120)

l2 = Label(m, text = "Enter Email", width = 10, font=("Times New Roman", 12))
l2.place(x = 19, y = 160)
e2 = Entry(m)
e2.place(x=200, y=160)

l3 = Label(m, text = "Contact number", width = 13, font=("Times New Roman", 12))
l3.place(x = 19, y = 200)
e3 = Entry(m)
e3.place(x=200, y=200)


l4 = Label(m, text = "Select Gender", width = 15, font=("Times New Roman", 12))
l4.place(x = 5, y = 240)
var = IntVar()
Radiobutton(m, text="Male", padx=5,variable=var, value=1).place(x=180, y=240)  
Radiobutton(m, text="Female", padx =10,variable=vars, value=2).place(x=240,y=240)
Radiobutton(m, text="Others", padx=15, variable=var,value=3).place(x=310,y=240)

list_of_country = ("India", "United States", "Germany", "Nepal")
cv = StringVar()
drplist=OptionMenu(m, cv, *list_of_country)
drplist.config(width=15)
cv.set("India")
l7 = Label(m, text="Select Country", width=13, font=("Times New Roman",12))
l7.place(x=14,y=280)
drplist.place(x=200,y=275)

l5 = Label(m, text = "Enter Password", width = 13, font=("Times New Roman", 12))
l5.place(x = 19, y = 320)
e5 = Entry(m,show='*')
e5.place(x=200, y=320)

l6 = Label(m, text = "Re-Enter Password", width = 15, font=("Times New Roman", 12))
l6.place(x = 21, y = 360)
e6 = Entry(m,show='*')
e6.place(x=200, y=360)

# Create a button for registration
register_button = Button(m, text="Register", width=10, command=register)
register_button.place(x=200, y=400)

m.mainloop()
