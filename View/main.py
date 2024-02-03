import tkinter as tk
import Controller.login as login
from tkinter import messagebox


class GUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.user_label = tk.Label(self, text="เลือกประเภทผู้ใช้") # Label : Just a text
        self.student_button = tk.Button(self, text="นักศึกษา") # Button : A button
        self.elderly_button = tk.Button(self, text="ผู้สูงอายุ") 
        self.child_button = tk.Button(self, text="เด็กโต")

        # button size
        self.student_button.config(height=5, width=20)
        self.elderly_button.config(height=5, width=20)
        self.child_button.config(height=5, width=20)

        # button click event
        self.student_button.config(command=self.student_button_click)
        self.elderly_button.config(command=self.elderly_button_click)
        self.child_button.config(command=self.child_button_click)

        # setup window title and size
        master.title("PEARLS")
        master.geometry("500x500")
        
        # pack the widgets
        self.user_label.pack()
        self.student_button.pack()
        self.elderly_button.pack()
        self.child_button.pack()
        
    def student_button_click(self):
        self.pack_forget()

        print("Enter username and password")

        # enter username and password via command line
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        # check if the username and password is correct
        result = login.check_credential(username, password)
        if result:
            # pop up a box if the login is success
            messagebox.showinfo("Login", "Login success")
            self.student_button_click()
        else:
            # pop up a box if the login is failed
            messagebox.showerror("Login", "Login failed")
            self.student_button_click()

    def elderly_button_click(self):
        # reset window and create elderly window in the main window
        self.pack_forget()
        self.elderly_window = ElderlyWindow(self.master)
        self.elderly_window.pack()

    def child_button_click(self):
        self.pack_forget()
        self.child_window = ChildWindow(self.master)
        self.child_window.pack()


class ElderlyWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # login form
        self.username_label = tk.Label(self, text="Username")
        self.username_entry = tk.Entry(self) # Entry : A text box
        self.password_label = tk.Label(self, text="Password")
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Login")

        self.username_label.pack()
        self.username_entry.pack(ipady=10, ipadx=10)
        self.password_label.pack()
        self.password_entry.pack(ipady=10, ipadx=10)
        self.login_button.pack()

        # setup text size and button size
        self.username_label.config(font=("Arial", 20))
        self.username_entry.config(font=("Arial", 20))
        self.password_label.config(font=("Arial", 20))
        self.password_entry.config(font=("Arial", 20))
        self.login_button.config(font=("Arial", 20))
        self.login_button.config(height=2, width=20)

        # button click event
        self.login_button.config(command=self.login_button_click)

    def login_button_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        result = login.check_credential(username, password)
        if result:
            messagebox.showinfo("Login", "Login success")
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
        else:
            messagebox.showerror("Login", "Login failed")
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')

class ChildWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)


        # login form
        self.username_label = tk.Label(self, text="Username")
        self.username_entry = tk.Entry(self) # Entry : A text box
        self.password_label = tk.Label(self, text="Password")
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Login")

        self.username_label.pack()
        self.username_entry.pack(ipady=5, ipadx=5)
        self.password_label.pack()
        self.password_entry.pack(ipady=5, ipadx=5)
        self.login_button.pack()

        # setup text size and button size
        self.username_label.config(font=("Arial", 8))
        self.username_entry.config(font=("Arial", 8))
        self.password_label.config(font=("Arial", 8))
        self.password_entry.config(font=("Arial", 8))
        self.login_button.config(font=("Arial", 8))
        self.login_button.config(height=2, width=18)

        # button click event
        self.login_button.config(command=self.login_button_click)

    def login_button_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        result = login.check_credential(username, password)
        if result:
            messagebox.showinfo("Login", "Login success")
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
        else:
            messagebox.showerror("Login", "Login failed")
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')

        



        
    

    