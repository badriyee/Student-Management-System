import tkinter as tk
from tkinter import messagebox, Frame, Label, Entry, Button
from PIL import ImageTk, Image
import os
import re
from tkinter import ttk





root = tk.Tk()
root.geometry('350x350')
root.configure(bg='red')
root.state('zoomed')
global login_photo
global home_photo


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
            
attendance_show = {}
if os.path.exists('attendance.txt'):
    with open('attendance.txt', 'r') as f:
        for line in f:
            data = line.strip().split(',')
            if len(data) == 4:
                firstname, lastname, week_number, status = data
                key = f"{firstname} {lastname}"
                if key not in attendance_show:
                    attendance_show[key] = []
                attendance_show[key].append((week_number, status))
payments = {}
if os.path.exists('payment.txt'):
    with open('payment.txt', 'r') as f:
        for line in f:
            data = line.strip().split(',')
            if len(data) == 4:
                firstname, lastname, payment_made, outstanding = data
            else:
                continue  # Skip lines with an unexpected number of values
            payments[f"{firstname} {lastname}"] = (payment_made, outstanding)



print(students)



def go_to_attendance():
     def exit(): 
        messagebox.showinfo(title='Signed Out', message = 'successfully exited')
        attend_frame.destroy()
        go_to_homescreen()
     def display(): 
         display_att = tk.Toplevel(root)
         display_att.geometry('500x500')
         display_att.title("Show Attendance")
         display_att.configure(bg= 'red')
         def show_records():
             firstname = firstname_entry.get()
             lastname = lastname_entry.get()
             key = f'{firstname} {lastname}'

             if key in attendance_show:
                for week, status in attendance_show[key]:
                  show_record_label = Label(display_att, text=f"Week {week}: {status}")
                  show_record_label.pack(pady=2)
             else:
                error_label = Label(display_att, text=f"No attendance data in system for {firstname} {lastname}")
                error_label.pack(pady=10)
        




         
         firstname_label = Label(display_att, text="First Name", width=20, font=("bold", 10), bg = 'red')
         firstname_entry = Entry(display_att, bg = 'black', fg = 'red')
         lastname_label = Label(display_att, text="Last Name", width=20, font=("bold", 10),bg = 'red')
         lastname_entry = Entry(display_att, fg='red', bg='black')
         submit_button = Button(display_att, text='Submit', width=20, bg='black', fg='red', command=show_records)
         firstname_label.pack(pady=10)
         firstname_entry.pack(pady=10)
         lastname_label.pack(pady=10)
         lastname_entry.pack(pady=10)
         submit_button.pack(pady=15)
         

   

    
     def attendance_register():
        attendance = tk.Toplevel(root)
        attendance.geometry('500x500')
        attendance.title("Mark Attendance")
        attendance.configure(bg = 'red')
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
                attendances[key] = status
                messagebox.showinfo(title='Success', message = 'Attendance has been saved.')
                attendance.destroy()
        firstname_label = Label(attendance, text="First Name", width=20, font=("bold", 10), bg='red')
        firstname_entry = Entry(attendance, bg='black', fg='red')
        lastname_label = Label(attendance, text="Last Name", width=20, font=("bold", 10), bg='red')
        lastname_entry = Entry(attendance, bg='black', fg='red')
        week_number_label = Label(attendance, text="Week", width=20, font=("bold", 10), bg='red')
        week_number_entry = ttk.Combobox(attendance, values=['1',  '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        status_label = Label(attendance, text="Present/Absent", width=20, font=("bold", 10), bg='red')
        status_entry = ttk.Combobox(attendance, values=["Present", "Absent"],)
        submit_button = Button(attendance, text='Submit', width=20, bg='black', fg='red', command=mark_attendance)
   

        firstname_label.pack(pady=10)
        firstname_entry.pack(pady=10)
        lastname_label.pack(pady=10)
        lastname_entry.pack(pady=10)
        week_number_label.pack(pady=10)
        week_number_entry.pack(pady=10)   
        status_label.pack(pady=10)
        status_entry.pack(pady=10)
        submit_button.pack(pady=20)  

     attend_frame = Frame(root, bg='black')
     attend_frame.pack()
     Fonts_tuple = ('Helvetica', 15, 'bold')
     Font_tuple = ('Helvetica', 30, 'bold') 
     welcome_label = tk.Label(attend_frame, text='Select', bg = 'black', fg= 'white' ,font = Font_tuple)
     attendance_button = tk.Button(attend_frame,text = 'Attendance', command= attendance_register, bg = 'red', fg = 'black', font = Fonts_tuple )
     display_button = tk.Button(attend_frame, text='Display Attendance', command= display, bg = 'red', fg = 'black' ,font = Fonts_tuple)
     exit_button = tk.Button(attend_frame, text='Exit', command= exit ,bg = 'red', fg = 'black' ,font = Fonts_tuple)
     welcome_label.pack( pady = 10, padx= 150)
     attendance_button.pack(pady= 90, padx=150)
     display_button.pack(pady=80, padx= 150)
     exit_button.pack(pady=100, padx=150)

def go_to_payment():
     def exit(): 
        messagebox.showinfo(title='Signed Out', message = 'successfully exited')
        payment_frame.destroy()
        go_to_homescreen()
     def display_paid():
         display_pay = tk.Toplevel(root) 
         display_pay.geometry('500x500')
         display_pay.title("Manage Payment")
         display_pay.configure(bg='red')
         def show_record():
            for key, value in payments.items():
              firstname, lastname = key.split()
              outstanding = value[1]
              if int(outstanding) != 0:
                  show_unpaid_label = Label(display_pay, text=f"{firstname} {lastname}: ${outstanding} unpaid", fg='black')
                  show_unpaid_label.pack(pady=10)
         show_button = Button(display_pay, text='Show Unpaid Students', width=20, bg='black', fg='red', command=show_record)
         show_button.pack(pady=15)
             
         
     def payment_manager():
        payment = tk.Toplevel(root) 
        payment.geometry('500x500')
        payment.title("Manage Payment")
        payment.configure(bg='red')
        def show_outstanding():
        
             firstname = firstname_entry.get()
             lastname = lastname_entry.get()
             key = f'{firstname} {lastname}'

             if key in payments:
                outstanding = payments[key][1]
                show_outstanding_label= Label(payment,text=f"Current Outstanding Amount: ${outstanding}", fg='black')
                show_outstanding_label.pack(pady=45)
        def update_payment():
            firstname = firstname_entry.get()
            lastname = lastname_entry.get()
            additional = additional_entry.get()

            key = f'{firstname} {lastname}'
            payment_made = payments[key][0]
            outstanding = payments[key][1]
            if key not in payments:
                messagebox.showinfo(title='Error', message = 'Student not found')
            else:

                payment_made = int(payment_made) + int(additional)
                outstanding = int(outstanding) - int(additional)
                with open('payment.txt', 'r') as f:
                    lines = f.readlines()
                with open('payment.txt', 'w') as f:
                    for line in lines:
                        if line.startswith(f'{firstname},{lastname}'):
                            f.write(f'{firstname},{lastname},{payment_made},{outstanding}\n')
                        else:
                            f.write(line)
                payments[key] = (payment_made, outstanding)
                messagebox.showinfo(title='Success', message = f'Payment Updated.\n New Oustanding Amount:${outstanding}')
                payment.destroy()
     

        firstname_label = Label(payment, text="First Name", width=20, font=("bold", 10), bg='red')
        firstname_entry = Entry(payment, bg='black', fg='red')
        lastname_label = Label(payment, text="Last Name", width=20, font=("bold", 10), bg='red')
        lastname_entry = Entry(payment, bg = 'black', fg='red')
        show_outstanding_button = Button(payment, text='Show Outstanding', command=show_outstanding)
        outstanding_label = Label(payment, text="Outstanding Amount: $", width=30, font=("bold", 10), bg='red')
        additional_label = Label(payment, text="Additional Payment", width=20, font=("bold", 10), bg='red')
        additional_entry = Entry(payment, bg='black', fg='red')  
        submit_button = Button(payment, text='Submit', command = update_payment, width=20, bg='black', fg='red')
 

        firstname_label.pack(pady=10)
        firstname_entry.pack(pady=5)
        lastname_label.pack(pady=10)
        lastname_entry.pack(pady=5)
        outstanding_label.pack(pady=10)  
        show_outstanding_button.pack(pady=5)    
        additional_label.pack(pady=10)
        additional_entry.pack(pady=5)
        submit_button.pack(pady=20) 

     payment_frame = Frame(root, bg='black')
     payment_frame.pack()
     Fonts_tuple = ('Helvetica', 15, 'bold') 
     Font_tuple = ('Helvetica', 30, 'bold') 
     welcome_label = tk.Label(payment_frame, text='Select Option', bg = 'black', fg= 'white' ,font = Font_tuple)
     payment_button = tk.Button(payment_frame,text = 'Update Payment', command= payment_manager, bg = 'black', fg = 'red', font = Fonts_tuple )
     display_button = tk.Button(payment_frame, text='Display Unpaid Students', command = display_paid , bg = 'black', fg = 'red' ,font = Fonts_tuple)
     exit_button = tk.Button(payment_frame, text='Exit', command= exit ,bg = 'black', fg = 'red' ,font = Fonts_tuple)
     welcome_label.pack( pady = 10, padx= 150)
     payment_button.pack(pady= 90, padx=150)
     display_button.pack(pady=80, padx= 150)
     exit_button.pack(pady=100, padx=150)



def go_to_homescreen():
    def exit(): 
        messagebox.showinfo(title='Signed Out', message = 'successfully exited')
        home_frame.destroy()
        welcome_frame.destroy()
        login_screen()
    def attendance_screen():
        home_frame.destroy()
        welcome_frame.destroy()
        go_to_attendance()
    def payment_screen():
        home_frame.destroy()
        welcome_frame.destroy()
        go_to_payment()



    def add_students():
        add = tk.Toplevel(root)
        add.geometry('500x500')  
        add.title("Manage Students") 
        add.configure(bg = 'red')
        def submit_student():
            firstname = firstname_entry.get()
            lastname = lastname_entry.get()
            address = address_entry.get()
            training_day = training_day_entry.get()
            payment_made = payment_made_entry.get()
            week_enrolled = week_enrolled_entry.get()
            training_weeks = (10 - int(week_enrolled))+1

            if firstname and lastname and address and training_day and payment_made:
                key = f"{firstname} {lastname}"
                students[key] = (address, training_day, payment_made)
                with open('students.txt', 'a') as f:
                    f.write(f'{firstname},{lastname},{address},{training_day},{payment_made}\n')
                with open('attendance.txt', 'a') as f:
                    
                    for i in range(1, training_weeks+1):
                        f.write(f'{firstname},{lastname},{i},present/absent\n')

                with open('payment.txt', 'a') as f:
                     term_payment = 45*(training_weeks)
                     outstanding = term_payment - int(payment_made)
                     f.write(f'{firstname},{lastname},{payment_made}, {outstanding}\n')
                payments[key] = (payment_made, outstanding)
                messagebox.showinfo(title='Success', message = 'Student details have been saved.')
                add.destroy()

        firstname_label = Label(add, text="First Name", width=20, font=("bold", 10), bg = 'red')
        firstname_entry = Entry(add, bg= 'black', fg= 'red')
        lastname_label = Label(add, text="Last Name", width=20, font=("bold", 10),bg = 'red')
        lastname_entry = Entry(add,bg='black', fg= 'red')
        address_label = Label(add, text="Address: House No., Street, Suburb, Postcode", width=20, font=("bold", 10),bg = 'red')
        address_entry = Entry(add,bg='black', fg= 'red')
        week_enrolled_label = Label(add, text="Week Enrolled", width=20, font=("bold", 10),bg = 'red')
        week_enrolled_entry = ttk.Combobox(add, values=['1', '2','3','4','5','6','7','8','9','10'])
        payment_made_label = Label(add, text="Payment Made ($)", width=20, font=("bold", 10),bg = 'red')
        payment_made_entry = Entry(add,bg='black', fg= 'red')
        training_day_label = Label(add, text="Training Day", width=20, font=("bold", 10),bg = 'red')
        training_day_entry = ttk.Combobox(add, values=[ "Monday",  "Tuesday","Wednesday", "Thursday","Friday"])
        submit_button = Button(add, text='Submit', width=20, bg='black', fg='red', command=submit_student)

        firstname_label.pack(pady=10)
        firstname_entry.pack(pady=5)
        lastname_label.pack(pady=10)
        lastname_entry.pack(pady=5)
        address_label.pack(pady=10)
        address_entry.pack(pady=5)
        training_day_label.pack(pady=10)
        training_day_entry.pack(pady=5)
        payment_made_label.pack(pady=10)
        payment_made_entry.pack(pady=5)
        week_enrolled_label.pack(pady=10)
        week_enrolled_entry.pack(pady=5)
        submit_button.pack(pady=10)
    def remove_student():
        removes = tk.Toplevel(root)
        removes.geometry('300x300')  
        removes.title("Remove Student") 
        removes.configure(bg='red')  

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
                removes.destroy()
        # existing code for setting up labels and entries

        remove_button = Button(removes, text='Remove', width=20, bg='black', fg='red', command=remove)
        firstname_label = Label(removes, text="First Name", width=20, font=("bold", 10), bg = 'red')
        firstname_entry = Entry(removes,bg='black', fg= 'red')
        lastname_label = Label(removes, text="Last Name", width=20, font=("bold", 10), bg = 'red')
        lastname_entry = Entry(removes,bg='black', fg= 'red')

        firstname_label.pack(pady=10)
        firstname_entry.pack(pady=10)
        lastname_label.pack(pady=10)
        lastname_entry.pack(pady=10)
        remove_button.pack(pady=20)
    def update_student():
        updates = tk.Toplevel(root)
        updates.geometry('500x500')  
        updates.title("Update Student")
        updates.configure(bg='red')  

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
                updates.destroy()

    # existing code for setting up labels and entries

        update_button = Button(updates, text='Update', width=20, bg='black', fg='red', command=update)
        firstname_label = Label(updates, text="First Name", width=20, font=("bold", 10), bg='red')
        firstname_entry = Entry(updates,bg='black', fg= 'red')
        lastname_label = Label(updates, text="Last Name", width=20, font=("bold", 10),bg='red')
        lastname_entry = Entry(updates,bg='black', fg= 'red')
        new_address_label = Label(updates, text="New Address", width=20, font=("bold", 10),bg='red')
        new_address_entry = Entry(updates,bg='black', fg= 'red')
        new_training_day_label = Label(updates, text="New Training Day", width=20, font=("bold", 10),bg='red')
        new_training_day_entry = ttk.Combobox(updates, values=["Monday", "Tuesday","Wednesday","Thursday", "Friday"],)

        firstname_label.pack(pady=10)
        firstname_entry.pack(pady=10)
        lastname_label.pack(pady=10)
        lastname_entry.pack(pady=10)
        new_address_label.pack(pady=10)
        new_address_entry.pack(pady=10)
        new_training_day_label.pack(pady=10)
        new_training_day_entry.pack(pady=10)
        update_button.pack(pady=20)



    global home_photo
    home_image_path = "step_up_correct.png"
    home_image = Image.open(home_image_path)
    home_photo = ImageTk.PhotoImage(home_image)
    home_frame = Frame(root, bg='black')
    home_frame.pack(side= 'left')
    welcome_frame = Frame(root, bg= 'red')
    welcome_frame.pack(side='top')
    home_image_label = Label(welcome_frame, image=home_photo, bg='red')
    home_image_label.pack(pady=20)
    

    Font_tuple = ("Helvetica", 30, "bold")   
    Fonts_tuple = ('Helvetica', 15, 'bold') 
    welcome_label = tk.Label(welcome_frame, text='Welcome, \nCoach!', bg = 'red', fg= 'black' ,font = Font_tuple)
    attendance_button = tk.Button(home_frame,text = '                                                        Attendance  ', command= attendance_screen, bg = 'white', fg = 'black', font = Fonts_tuple )
    payment_button = tk.Button(home_frame, text= '                                                           Payments  ', command=payment_screen, bg = 'white', fg = 'black' ,font = Fonts_tuple)
    add_button = tk.Button(home_frame, text= '                                                    Add Students  ', command = add_students, bg = 'white', fg = 'black' ,font = Fonts_tuple)
    remove_button = tk.Button(home_frame, text= '                                              Remove Students  ', command = remove_student , bg = 'white', fg = 'black' ,font = Fonts_tuple)
    update_button = tk.Button(home_frame, text= '                                               Update Students  ', command = update_student , bg = 'white', fg = 'black' ,font = Fonts_tuple)
    exit_button = tk.Button(home_frame, command = exit, text = '                                                      Exit  ', bg = 'white', fg = 'black', font= Fonts_tuple)

    welcome_label.pack()
    attendance_button.pack(pady=40)
    payment_button.pack(pady=40)
    add_button.pack(pady=40)
    remove_button.pack(pady= 40)
    update_button.pack( pady = 40)
    exit_button.pack( pady = 40)
   

# Function for user registration
def registration():
    register = tk.Toplevel(root)
    register.geometry('500x500')  
    register.title("Registration Form")  
    register.configure(bg='red') 

    def submit_registration():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        # Check if the password and confirm password match
        if password != confirm_password:
            messagebox.showinfo(title='Registration Unsuccssful', message = 'Passwords do not match')
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

    username_label = Label(register, text="Username", width=20, font=("bold", 10), bg = 'red')
    username_entry = Entry(register,bg='black', fg= 'red')
    email_label = Label(register, text="Email", width=20, font=("bold", 10),bg = 'red')
    email_entry = Entry(register,bg='black', fg= 'red')
    password_label = Label(register, text="Password", width=20, font=("bold", 10),bg = 'red')
    password_entry = Entry(register, show='*',bg='black', fg= 'red')
    confirm_password_label = Label(register, text="Confirm Password", width=20, font=("bold", 10),bg = 'red')
    confirm_password_entry = Entry(register, show='*', bg='black', fg='red')
    submit_button = Button(register, text='Submit', width=20, bg='black', fg='red', command=submit_registration)

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
    global login_photo

    def login():
        username = username_entry.get()
        password = password_entry.get()
        
        if username in users and users[username][1] == password:
            messagebox.showinfo(title='Login Success!', message = 'Successfully logged in')
            frame.pack_forget()
            img.pack_forget()
            go_to_homescreen()
        else:
            messagebox.showinfo(title='Login Failed!', message = 'Incorrect username or password')
    login_image_path = "gang.png"
    login_image = Image.open(login_image_path)
    login_photo = ImageTk.PhotoImage(login_image)

    frame = Frame(root, bg='black',width=200, height=450)
    frame.pack(padx = 80,pady= 100, side= 'right')
    img = Frame(root, bg='red')
    img.pack(side='left')
    word = Frame(root, bg='red')
    word.pack(side='left')
    login_image_label = Label(img, image=login_photo, bg='red')
    stepup_label = Label(img, text = 'Step \n  Up\nBasketball\n      Academy', fg = 'black', bg = 'red',  font=('Segoe UI Black', 25))
    stepup_label.pack(padx=30)
    login_image_label.pack(pady=20, padx=50)
   
    login_label = Label(frame, text = 'Login', fg = 'red', bg = 'black',  font=('Haettenschweiler', 25))
    username_label = Label(frame, text = 'Username', fg = 'red', bg = 'black', font=('Haettenschweiler', 16))
    password_label = Label(frame, text='Password',fg = 'red', bg = 'black', font=('Haettenschweiler',15))
    username_entry = Entry(frame, font=('Helvetica', 10),bg='black', fg= 'red')
    password_entry = Entry(frame, show='*', font=('Helvetica', 10),bg='black', fg= 'red')
    login_button = Button(frame, command = login,font=('Haettenschweiler',10),text = 'Login', bg = 'black', fg = 'red')
    register_button = Button(frame, command = registration, font=('Haettenschweiler',10),text = "Don't have an account?", bg = 'black', fg = 'red')
    login_label.pack(pady=10, padx= 100)
    username_label.pack(pady=60, padx=100)
    username_entry.pack(padx= 20)
    password_label.pack(pady=40, padx= 100)
    password_entry.pack(padx = 20)
    login_button.pack(pady=30, padx= 100)
    register_button.pack(pady=10, padx= 100)


print(attendances)
login_screen()
root.mainloop()
