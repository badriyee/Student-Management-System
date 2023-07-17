import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('440x440')
root.configure(bg='red')
root.state('zoomed')

def go_to_homescreen():
    home_frame = Frame(root, bg='red')
    home_frame.pack()
    img =Image.open('Untitled.png')
    photo1 = ImageTk.PhotoImage(img)
    img_label = Label(home_frame, image=photo1, bg='black')
    img_label.image = photo1
    img_label.place(x=5,y=5)
    img_label.size(500,500)

    welcome_label = tk.Label(home_frame, text='Welcome', bg = 'red', fg= 'black' ,font = ('Tekton Pro', 30))
    username_label = tk.Label(home_frame, text = 'Username', bg = 'red',font = ('Tekton Pro', 16))
    password_label = tk.Label(home_frame, text='Password', bg = 'red', font = ('Tekton Pro',16))
    username_entry = tk.Entry(home_frame, text = '',font = ('Tekton Pro', 16))
    password_entry = tk.Entry(home_frame, show='*',font = ('Tekton Pro', 16))
    login_button = tk.Button(home_frame,text = 'Login', bg = 'black', fg = 'red')

    # login_label.grid(row=1, column =0, columnspan=2, pady = 40 )
    username_label.grid(row = 2, column= 0, pady = 10)
    username_entry.grid(row = 2, column= 1, padx = 15, pady= 10)
    password_label.grid(row = 3, column= 0)
    password_entry.grid(row = 3, column= 1, padx = 15)
    login_button.grid(row= 4, column= 0, columnspan = 2, pady = 30)
    



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

   

    login_label = tk.Label(frame, text='Login', bg = 'red', font = ('Tekton Pro', 30))
    username_label = tk.Label(frame, text = 'Username', bg = 'red',font = ('Tekton Pro', 16))
    password_label = tk.Label(frame, text='Password', bg = 'red', font = ('Tekton Pro',16))
    username_entry = tk.Entry(frame, text = '',font = ('Tekton Pro', 16))
    password_entry = tk.Entry(frame, show='*',font = ('Tekton Pro', 16))
    login_button = tk.Button(frame, command = login,text = 'Login', bg = 'black', fg = 'red')
    
    login_label.grid(row=1, column =0, columnspan=2, pady = 40 )
    username_label.grid(row = 2, column= 0, pady = 10)
    username_entry.grid(row = 2, column= 1, padx = 15, pady= 10)
    password_label.grid(row = 3, column= 0)
    password_entry.grid(row = 3, column= 1, padx = 15)
    login_button.grid(row= 4, column= 0, columnspan = 2, pady = 30)
    frame.pack()

login_screen()

root.mainloop()

