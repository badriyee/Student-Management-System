import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import xml.etree.ElementTree as ET
from tkinter import filedialog
import os
root = tk.Tk()
root.geometry('440x440')
root.configure(bg='red')
root.state('zoomed')




#new_account = ET.SubElement(root, "account")
#new_username = ET.SubElement(new_account, "username")
#new_password = ET.SubElement(new_account, "password")
#new_username.text = "Badri"
#new_password.text = "1234"

#tree.write("users.xml")






def attendance(day):
    attendance_frame = Frame(root, bg= 'red')
    attendance_frame.pack()
    with open('students.txt', 'r') as f:
        students = [line.strip() for line in f]

    # Create checkboxes for attendance
    student_vars = {name: tk.BooleanVar() for name in students}
    for student, var in student_vars.items():
        cb = tk.Checkbutton(attendance_frame, text=student, variable=var, onvalue=True, offvalue=False, bg='red', fg='white')
        cb.pack(anchor='w')

    def submit_attendance():
        for student, var in student_vars.items():
            print(f'{student}: {"Present" if var.get() else "Absent"}')  # replace with your attendance logic
    
    # Button to submit attendance
    submit_button = tk.Button(attendance_frame, text='Submit Attendance', command=submit_attendance, bg = 'black', fg = 'red')
    submit_button.pack()
    
   

def payment():
    payment_frame = Frame(root, bg = 'red')
    payment_frame.pack()
    
   
    Fonts_tuple = ('Helvetica', 50, 'bold') 
    welcome_label = tk.Label(payment_frame, text='Welcome, \nCoach!', bg = 'red', fg= 'black' ,font = Fonts_tuple)
    
     #login_label.grid(row=1, column =0, columnspan=2, pady = 40 )
    welcome_label.grid(row = 10, column= 150, pady = 10)
def attendance_days():
    def switch_to_attendance(day):
        days_frame.destroy()
        welcome_frame.destroy()
        bottom_frame.destroy()
        attendance(day)
    def exit(): 
        messagebox.showinfo(title='Signged Out', message = 'successfully exited')
        days_frame.destroy()
        welcome_frame.destroy()
        bottom_frame.destroy()
        go_to_homescreen()
    days_frame = Frame(root, bg='red')
    days_frame.pack()
    welcome_frame = Frame(root, bg= 'red')
    welcome_frame.pack()
    bottom_frame = Frame(root, bg= 'red')
    bottom_frame.pack(side='bottom')
        
    Fonts_tuple = ('Helvetica', 15, 'bold') 
    days_label = tk.Label(days_frame, text='Select Training Day!', bg = 'red', fg= 'black' ,font = Fonts_tuple)
    day1_button = tk.Button(welcome_frame,command = switch_to_attendance(day='monday'),text = 'Monday', bg = 'black', fg = 'red', font = Fonts_tuple )
    day2_button = tk.Button(welcome_frame, text='Tuesday', command = switch_to_attendance, bg = 'black', fg = 'red' ,font = Fonts_tuple)
    day3_button = tk.Button(welcome_frame,command = switch_to_attendance,text = 'Wednesday', bg = 'black', fg = 'red', font = Fonts_tuple )
    day4_button = tk.Button(welcome_frame, text='Thursday', command = switch_to_attendance, bg = 'black', fg = 'red' ,font = Fonts_tuple)
    day5_button = tk.Button(welcome_frame, text='Friday', command = switch_to_attendance, bg = 'black', fg = 'red' ,font = Fonts_tuple)
    exit_button = tk.Button(bottom_frame, command = exit, text = 'Exit', bg = 'black', fg = 'red', font= Fonts_tuple)

    days_label.pack()
    day1_button.grid(row = 4, column= 10,  pady= 15)
    day2_button.grid(row = 5, column= 10, pady=5)
    day3_button.grid(row = 6, column= 10, pady= 5)
    day4_button.grid(row = 7, column= 10, pady=5)
    day5_button.grid(row = 8, column= 10, pady= 5)
    
    exit_button.grid(row = 20, column= 50, pady = 100)
    


def payment_days():
    def switch_to_payment(day):
        days_frame.destroy()
        welcome_frame.destroy()
        bottom_frame.destroy()
        payment(day)
    def exit(): 
        messagebox.showinfo(title='Signged Out', message = 'successfully exited')
        days_frame.destroy()
        welcome_frame.destroy()
        bottom_frame.destroy()
        go_to_homescreen()

    days_frame = Frame(root, bg='red')
    days_frame.pack()
    welcome_frame = Frame(root, bg= 'red')
    welcome_frame.pack()
    bottom_frame = Frame(root, bg= 'red')
    bottom_frame.pack(side='bottom')
        
    Fonts_tuple = ('Helvetica', 25, 'bold') 
    days_label = tk.Label(days_frame, text='Select Training Day!', bg = 'red', fg= 'black' ,font = Fonts_tuple)
    day1_button = tk.Button(welcome_frame,command = switch_to_payment,text = 'Monday', bg = 'black', fg = 'red', font = Fonts_tuple )
    day2_button = tk.Button(welcome_frame, text='Tuesday', command = switch_to_payment, bg = 'black', fg = 'red' ,font = Fonts_tuple)
    day3_button = tk.Button(welcome_frame,command = switch_to_payment,text = 'Wednesday', bg = 'black', fg = 'red', font = Fonts_tuple )
    day4_button = tk.Button(welcome_frame, text='Thursday', command = switch_to_payment, bg = 'black', fg = 'red' ,font = Fonts_tuple)
    day5_button = tk.Button(welcome_frame, text='Friday', command = switch_to_payment, bg = 'black', fg = 'red' ,font = Fonts_tuple)
    exit_button = tk.Button(bottom_frame, command = exit, text = 'Exit', bg = 'black', fg = 'red', font= Fonts_tuple)

    days_label.pack()
    day1_button.grid(row = 4, column= 10,  pady= 15)
    day2_button.grid(row = 5, column= 10, pady=5)
    day3_button.grid(row = 6, column= 10, pady= 5)
    day4_button.grid(row = 7, column= 10, pady=5)
    day5_button.grid(row = 8, column= 10, pady= 5)
    
    exit_button.grid(row = 20, column= 50, pady = 100)
    


def go_to_homescreen():
    def exit(): 
        messagebox.showinfo(title='Signged Out', message = 'successfully exited')
        home_frame.destroy()
        welcome_frame.destroy()
        bottom_frame.destroy()
        login_screen()
    
    def switch_to_attendances():
        home_frame.destroy()
        welcome_frame.destroy()
        bottom_frame.destroy()
        attendance_days()
        

    def switch_to_payments():
        home_frame.destroy()
        welcome_frame.destroy()
        bottom_frame.destroy()
        payment_days()

    home_frame = Frame(root, bg='red')
    home_frame.place(x=25, y=100)
    welcome_frame = Frame(root, bg= 'red')
    welcome_frame.pack(side='right', padx = 250, pady=250)
    bottom_frame = Frame(root, bg= 'red')
    bottom_frame.pack(side='bottom')

    Font_tuple = ("Helvetica", 20, "bold")   
    Fonts_tuple = ('Helvetica', 50, 'bold') 
    welcome_label = tk.Label(welcome_frame, text='Welcome, \nCoach!', bg = 'red', fg= 'black' ,font = Fonts_tuple)
    attendance_button = tk.Button(home_frame,command = switch_to_attendances,text = 'Attendance', bg = 'black', fg = 'red', font = Font_tuple )
    payment_button = tk.Button(home_frame, text='Payment', command = switch_to_payments, bg = 'black', fg = 'red' ,font = Font_tuple)
    exit_button = tk.Button(bottom_frame, command = exit, text = 'Exit', bg = 'black', fg = 'red', font= Font_tuple)

    welcome_label.grid(row = 10, column= 150, pady = 10)
    attendance_button.grid(row = 4, column= 0, padx = 15, pady= 10)
    payment_button.grid(row = 5, column= 0, pady=50)
    exit_button.grid(row = 20, column= 50, pady = 100)
   
 
def registration():
    base = Tk()  
    base.geometry('500x500')  
    base.title("Registration Form")  
  
    labl_0 = Label(base, text="Registration form",width=20,font=("bold", 20))  
    labl_0.place(x=90,y=53)  
  
  
    labl_1 = Label(base, text="FullName",width=20,font=("bold", 10))  
    labl_1.place(x=80,y=130)  
  
    entry_1 = Entry(base)  
    entry_1.place(x=240,y=130)  
  
    labl_2 = Label(base, text="Email",width=20,font=("bold", 10))  
    labl_2.place(x=68,y=180)  
  
    entry_02 = Entry(base)  
    entry_02.place(x=240,y=180)  
    labl_4 = Label(base, text="Age:",width=20,font=("bold", 10))  
    labl_4.place(x=70,y=280)  
  
  
    entry_02 = Entry(base)  
    entry_02.place(x=240,y=280)  
      
     
  
    Button(base, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)  
# it will be used for displaying the registration form onto the window  
    base.mainloop()  


def login_screen():
    def login():
        
        username = 'Head Coach'
        password = '1234'
        if username_entry.get()== username and password_entry.get() == password:
            messagebox.showinfo(title='Login Success!', message = 'successfully logged in')
            frame.pack_forget()
            go_to_homescreen()
        else:
            messagebox.showinfo(title='Login Failed!', message = 'incorrect username or password')

    frame = Frame(root, bg='red')
    frame.pack()

    Font_tuple = ("Helvetica", 20, "bold")
    login_label = tk.Label(frame, text='Login', bg = 'red', font = Font_tuple)
    username_label = tk.Label(frame, text = 'Username', bg = 'red',font = ('Tekton Pro', 16))
    password_label = tk.Label(frame, text='Password', bg = 'red', font = ('Tekton Pro',16))
    username_entry = tk.Entry(frame, text = '',font = ('Tekton Pro', 16))
    password_entry = tk.Entry(frame, show='*',font = ('Tekton Pro', 16))
    login_button = tk.Button(frame, command = login,text = 'Login', bg = 'black', fg = 'red')
    register_button = tk.Button(frame, command = registration,text = "don't have an account?", bg = 'black', fg = 'red')
    
    login_label.grid(row=1, column =0, columnspan=2, pady = 40 )
    username_label.grid(row = 2, column= 0, pady = 10)
    username_entry.grid(row = 2, column= 1, padx = 15, pady= 10)
    password_label.grid(row = 3, column= 0)
    password_entry.grid(row = 3, column= 1, padx = 15)
    login_button.grid(row= 4, column= 0, columnspan = 2, pady = 30)
    register_button.grid(row= 5, column= 0, columnspan = 2, pady = 30)
    frame.pack()

login_screen()

root.mainloop()

