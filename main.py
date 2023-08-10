import tkinter as tk
from tkinter import messagebox, Frame, Label, Entry, Button
from PIL import ImageTk, Image
import os
import re
from tkinter import ttk



# Initiate main tkinter window
root = tk.Tk()
root.geometry('440x440')
root.configure(bg='red')
root.state('zoomed')

# File to store registered users
user_file = 'users.txt'

# Load registered users from the file
users = {}
if os.path.exists(user_file):
    with open(user_file, 'r') as f:
        for line in f:
            username, email, password = line.strip().split(',')
            users[username] = (email, password)

students = {}
if os.path.exists('students.txt'):
    with open('students.txt', 'r') as f:
        for line in f:
            data = line.strip().split(',')
            if len(data) == 4:
                firstname, lastname, address, training_day = data
                payment_made = '0'  # Use a default value for older entries
            elif len(data) == 5:
                firstname, lastname, address, training_day, payment_made = data
            else:
                continue  # Skip lines with an unexpected number of values
            students[f"{firstname} {lastname}"] = (address, training_day, payment_made)

attendances = {}
if os.path.exists('attendance.txt'):
    with open('attendance.txt', 'r') as f:
        for line in f:
            data = line.strip().split(',')
            if len(data) == 4:
                firstname, lastname, week_number, status = data
            else:
                continue  # Skip lines with an unexpected number of values
            attendances[f"{firstname} {lastname} {week_number}"] = (status)



print(students)



    
    




def go_to_homescreen():
    def exit(): 
        messagebox.showinfo(title='Signed Out', message = 'successfully exited')
        home_frame.destroy()
        welcome_frame.destroy()
        bottom_frame.destroy()
        login_screen()
    def attendance_register():
        attendance = tk.Toplevel(root)
        attendance.geometry('500x500')
        attendance.title("Mark Attendance")
        def mark_attendance():
            
            firstname = firstname_entry.get()
            lastname = lastname_entry.get()
            week_number = week_number_entry.get()
            status = status_entry.get()
            key = f'{firstname} {lastname} {week_number}'
    
            if key not in attendances:
                messagebox.showinfo(title='Error', message = 'Student not found')
            else:
                with open('attendance.txt', 'r') as f:
                    lines = f.readlines()
                with open('attendance.txt', 'w') as f:
                    for line in lines:
                        if line.startswith(f'{firstname},{lastname},{week_number}'):
                            f.write(f'{firstname},{lastname},{week_number},{status}\n')
                        else:
                            f.write(line)
                messagebox.showinfo(title='Success', message = 'Attendance has been saved.')
                attendance.destroy()
        firstname_label = Label(attendance, text="First Name", width=20, font=("bold", 10))
        firstname_entry = Entry(attendance)
        lastname_label = Label(attendance, text="Last Name", width=20, font=("bold", 10))
        lastname_entry = Entry(attendance)
        week_number_label = Label(attendance, text="Week", width=20, font=("bold", 10))
        week_number_entry = ttk.Combobox(attendance, 
                                        values=[
                                            '1', 
                                            '2',
                                            '3',
                                            '4',
                                            '5',
                                            '6',
                                            '7',
                                            '8',
                                            '9',
                                            '10'])
        status_label = Label(attendance, text="Present/Absent", width=20, font=("bold", 10))
        status_entry = Entry(attendance)
        submit_button = Button(attendance, text='Submit', width=20, bg='brown', fg='white', command=mark_attendance)
   

        firstname_label.pack(pady=10)
        firstname_entry.pack(pady=10)
        lastname_label.pack(pady=10)
        lastname_entry.pack(pady=10)
        week_number_label.pack(pady=10)
        week_number_entry.pack(pady=10)   
        status_label.pack(pady=10)
        status_entry.pack(pady=10)
        submit_button.pack(pady=20)       
    def payment_manager():
        payment = tk.Toplevel(root) 
        payment.geometry('500x500')
        payment.title("Manage Payment")
        def update_payment():
            firstname = firstname_entry.get()
            lastname = lastname_entry.get()
            additional = additional_entry.get()

            key = f'{firstname} {lastname}'
            payment_made = students[key][2]
            if key not in students:
                messagebox.showinfo(title='Error', message = 'Student not found')
            else:

                payment_made = int(payment_made) + int(additional)
                outstanding = 450 - int(payment_made)
                with open('payment.txt', 'r') as f:
                    lines = f.readlines()
                with open('payment.txt', 'w') as f:
                    for line in lines:
                        if line.startswith(f'{firstname},{lastname}'):
                            f.write(f'{firstname},{lastname},{payment_made},{outstanding}\n')
                        else:
                            f.write(line)
                messagebox.showinfo(title='Success', message = f'Payment Updated.\n New Oustanding Amount:${outstanding}')
                payment.destroy()
            
        firstname_label = Label(payment, text="First Name", width=20, font=("bold", 10))
        firstname_entry = Entry(payment)
        lastname_label = Label(payment, text="Last Name", width=20, font=("bold", 10))
        lastname_entry = Entry(payment)
        additional_label = Label(payment, text="Additional Payment", width=20, font=("bold", 10))
        additional_entry = Entry(payment)  
        submit_button = Button(payment, text='Submit', command = update_payment, width=20, bg='brown', fg='white',)
 

        firstname_label.pack(pady=10)
        firstname_entry.pack(pady=10)
        lastname_label.pack(pady=10)
        lastname_entry.pack(pady=10)
 
        additional_label.pack(pady=10)
        additional_entry.pack(pady=10)
        submit_button.pack(pady=20) 

    def manage_students():
        base = tk.Toplevel(root)
        base.geometry('500x500')  
        base.title("Manage Students") 
        def submit_student():
            firstname = firstname_entry.get()
            lastname = lastname_entry.get()
            address = address_entry.get()
            training_day = training_day_entry.get()
            payment_made = payment_made_entry.get()

            if firstname and lastname and address and training_day and payment_made:
                key = f"{firstname} {lastname}"
                students[key] = (address, training_day, payment_made)
                with open('students.txt', 'a') as f:
                    f.write(f'{firstname},{lastname},{address},{training_day},{payment_made}\n')
                with open('attendance.txt', 'a') as f:
                    for i in range(1, 11):
                        f.write(f'{firstname},{lastname},{i},present/absent\n')

                with open('payment.txt', 'a') as f:
                     outstanding = 450 - int(payment_made)
                     f.write(f'{firstname},{lastname},{payment_made}, {outstanding}\n')
                messagebox.showinfo(title='Success', message = 'Student details have been saved.')
                base.destroy()

        firstname_label = Label(base, text="First Name", width=20, font=("bold", 10))
        firstname_entry = Entry(base)
        lastname_label = Label(base, text="Last Name", width=20, font=("bold", 10))
        lastname_entry = Entry(base)
        address_label = Label(base, text="Address", width=20, font=("bold", 10))
        address_entry = Entry(base)
        training_day_label = Label(base, text="Training Day", width=20, font=("bold", 10))
        training_day_entry = ttk.Combobox(base, 
                                        values=[
                                            "Monday", 
                                            "Tuesday",
                                            "Wednesday",
                                            "Thursday",
                                            "Friday"])
        payment_made_label = Label(base, text="Payment Made", width=20, font=("bold", 10))
        payment_made_entry = Entry(base)
        submit_button = Button(base, text='Submit', width=20, bg='brown', fg='white', command=submit_student)

        firstname_label.pack(pady=10)
        firstname_entry.pack(pady=10)
        lastname_label.pack(pady=10)
        lastname_entry.pack(pady=10)
        address_label.pack(pady=10)
        address_entry.pack(pady=10)
        training_day_label.pack(pady=10)
        training_day_entry.pack(pady=10)
        payment_made_label.pack(pady=10)
        payment_made_entry.pack(pady=10)
        submit_button.pack(pady=20)
    def remove_student():
        base = tk.Toplevel(root)
        base.geometry('500x500')  
        base.title("Remove Student") 

        def remove():
            

            firstname = firstname_entry.get()
            lastname = lastname_entry.get()

            key = f'{firstname} {lastname}'

            if key not in students:
                messagebox.showinfo(title='Remove Failed', message = 'Student not found')
            else:
                del students[key]
                with open('students.txt', 'w') as f:
                    for name, details in students.items():
                        f.write(f'{name},{",".join(details)}\n')
                        
        # Update attendance.txt
                with open('attendance.txt', 'r') as f:
                    lines = f.readlines()
                with open('attendance.txt', 'w') as f:
                    for line in lines:
                        if not line.startswith(f'{firstname},{lastname}'):
                            f.write(line)
        # Update payment.txt
                with open('payment.txt', 'r') as f:
                    lines = f.readlines()
                with open('payment.txt', 'w') as f:
                    for line in lines:
                        if not line.startswith(f'{firstname},{lastname}'):
                             f.write(line)
                messagebox.showinfo(title='Success', message = 'Student details have been removed.')
                base.destroy()
        # existing code for setting up labels and entries

        remove_button = Button(base, text='Remove', width=20, bg='brown', fg='white', command=remove)
        remove_button.pack(pady=20)
        firstname_label = Label(base, text="First Name", width=20, font=("bold", 10))
        firstname_entry = Entry(base)
        lastname_label = Label(base, text="Last Name", width=20, font=("bold", 10))
        lastname_entry = Entry(base)

        firstname_label.pack(pady=10)
        firstname_entry.pack(pady=10)
        lastname_label.pack(pady=10)
        lastname_entry.pack(pady=10)
    def update_student():
        base = tk.Toplevel(root)
        base.geometry('500x500')  
        base.title("Update Student") 

        def update():
            firstname = firstname_entry.get()
            lastname = lastname_entry.get()
            new_address = new_address_entry.get()
            new_training_day = new_training_day_entry.get()
            #new_payment_made = new_payment_made_entry.get()

            key = f'{firstname} {lastname}'
            

            if key not in students:
                messagebox.showinfo(title='Update Failed', message = 'Student not found')
            else:
                students[key] = (new_address, new_training_day,students[key][2])
                with open('students.txt', 'r') as f:
                    lines = f.readlines()
                with open('students.txt', 'w') as f:
                    for line in lines:
                        if line.startswith(f'{firstname},{lastname}'):
                            f.write(f'{firstname}, {lastname},{new_address},{new_training_day},{students[key][2]}\n')
                        else:
                            f.write(line)
                
                messagebox.showinfo(title='Success', message = 'Student details have been updated.')
                base.destroy()

    # existing code for setting up labels and entries

        update_button = Button(base, text='Update', width=20, bg='brown', fg='white', command=update)
        update_button.pack(pady=20)
        firstname_label = Label(base, text="First Name", width=20, font=("bold", 10))
        firstname_entry = Entry(base)
        lastname_label = Label(base, text="Last Name", width=20, font=("bold", 10))
        lastname_entry = Entry(base)
        new_address_label = Label(base, text="New Address", width=20, font=("bold", 10))
        new_address_entry = Entry(base)
        new_training_day_label = Label(base, text="New Training Day", width=20, font=("bold", 10))
        new_training_day_entry = ttk.Combobox(base, 
                                        values=[
                                            "Monday", 
                                            "Tuesday",
                                            "Wednesday",
                                            "Thursday",
                                            "Friday"])

        firstname_label.pack(pady=10)
        firstname_entry.pack(pady=10)
        lastname_label.pack(pady=10)
        lastname_entry.pack(pady=10)
        new_address_label.pack(pady=10)
        new_address_entry.pack(pady=10)
        new_training_day_label.pack(pady=10)
        new_training_day_entry.pack(pady=10)




    home_frame = Frame(root, bg='red')
    home_frame.place(x=25, y=100)
    welcome_frame = Frame(root, bg= 'red')
    welcome_frame.pack(side='right', padx = 250, pady=250)
    bottom_frame = Frame(root, bg= 'red')
    bottom_frame.pack(side='bottom')

    Font_tuple = ("Helvetica", 20, "bold")   
    Fonts_tuple = ('Helvetica', 15, 'bold') 
    welcome_label = tk.Label(welcome_frame, text='Welcome, \nCoach!', bg = 'red', fg= 'black' ,font = Fonts_tuple)
    attendance_button = tk.Button(home_frame,text = 'Attendance', command= attendance_register, bg = 'black', fg = 'red', font = Fonts_tuple )
    payment_button = tk.Button(home_frame, text='Payment', command=payment_manager, bg = 'black', fg = 'red' ,font = Font_tuple)
    add_button = tk.Button(home_frame, text='Add Students', command = manage_students, bg = 'black', fg = 'red' ,font = Fonts_tuple)
    remove_button = tk.Button(home_frame, text='Remove Students', command = remove_student , bg = 'black', fg = 'red' ,font = Fonts_tuple)
    update_button = tk.Button(home_frame, text='Update Students', command = update_student , bg = 'black', fg = 'red' ,font = Fonts_tuple)
    exit_button = tk.Button(bottom_frame, command = exit, text = 'Exit', bg = 'black', fg = 'red', font= Font_tuple)

    welcome_label.grid(row = 10, column= 150, pady = 10)
    attendance_button.grid(row = 2, column= 0, padx = 5, pady= 10)
    payment_button.grid(row = 3, column= 0, pady=5)
    add_button.grid(row = 4, column= 0, pady=5)
    remove_button.grid(row=5, column= 0, pady = 5)
    update_button.grid(row = 6, column = 0, pady = 5)
    exit_button.grid(row = 7, column= 0, pady = 10)
   

# Function for user registration
def registration():
    register = tk.Toplevel(root)
    register.geometry('500x500')  
    register.title("Registration Form")  

    def submit_registration():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        # Check if the password and confirm password match
        if password != confirm_password:
            messagebox.showinfo(title='Registration Failed', message = 'Passwords do not match.')
            return

        # Check if the password meets the strength requirements
        if len(password) < 8 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password):
            messagebox.showinfo(title='Registration Failed', message = 'Password should be at least 8 characters long and should contain at least one lowercase letter, one uppercase letter and one digit.')
            return

        if username and email and password:
            users[username] = (email, password)
            with open(user_file, 'a') as f:
                f.write(f'{username},{email},{password}\n')
            messagebox.showinfo(title='Registration Success', message = 'You have successfully registered. You can now log in with your credentials.')
            register.destroy()

    username_label = Label(register, text="Username", width=20, font=("bold", 10))
    username_entry = Entry(register)
    email_label = Label(register, text="Email", width=20, font=("bold", 10))
    email_entry = Entry(register)
    password_label = Label(register, text="Password", width=20, font=("bold", 10))
    password_entry = Entry(register, show='*')
    confirm_password_label = Label(register, text="Confirm Password", width=20, font=("bold", 10))
    confirm_password_entry = Entry(register, show='*')
    submit_button = Button(register, text='Submit', width=20, bg='brown', fg='white', command=submit_registration)

    username_label.pack(pady=10)
    username_entry.pack(pady=10)
    email_label.pack(pady=10)
    email_entry.pack(pady=10)
    password_label.pack(pady=10)
    password_entry.pack(pady=10)
    confirm_password_label.pack(pady=10)
    confirm_password_entry.pack(pady=10)
    submit_button.pack(pady=20)

# Function for user login
def login_screen():
    def login():
        username = username_entry.get()
        password = password_entry.get()
        
        if username in users and users[username][1] == password:
            messagebox.showinfo(title='Login Success!', message = 'Successfully logged in')
            frame.pack_forget()
            go_to_homescreen()
        else:
            messagebox.showinfo(title='Login Failed!', message = 'Incorrect username or password')

    frame = Frame(root, bg='red')
    frame.pack()

    username_label = Label(frame, text = 'Username', bg = 'red', font=('Helvetica', 16))
    password_label = Label(frame, text='Password', bg = 'red', font=('Helvetica',16))
    username_entry = Entry(frame, font=('Helvetica', 16))
    password_entry = Entry(frame, show='*', font=('Helvetica', 16))
    login_button = Button(frame, command = login, text = 'Login', bg = 'black', fg = 'red')
    register_button = Button(frame, command = registration, text = "Don't have an account?", bg = 'black', fg = 'red')

    username_label.pack(pady=10)
    username_entry.pack(pady=10)
    password_label.pack(pady=10)
    password_entry.pack(pady=10)
    login_button.pack(pady=20)
    register_button.pack(pady=10)



login_screen()
root.mainloop()
