import tkinter as tk
m=tk.Tk()
m.geometry('200x200') 
m.title('Login')
l1=Label(m,text='username')
l1.pack(x=50,y=60)
l2=Label(m,text='password')
l2.pack()
e1=Entry(m)
e2=Entry(m)
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)
def fun():
    new=Tk()
    l3=Label(new,text='Login Successfully!!')

    
button=tk.Button(m,text='Login',command=fun)
button.pack()

m.mainloop()
