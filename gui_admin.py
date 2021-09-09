from Node import Node
from Person import Person
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk

class gui_admin:
    ADMIN_ERROR_TEXT = [
        " ",
        "Incorect Cridentials",
        "Not Logged In",
    ]
    def __init__(self,master,node,username,password,filename):
        self.master = master
        
        self.login = False
        
        master.title("Input Form-Admin")
        
        self.label_error_index2 = 0
        self.label_error_text2 = StringVar()
        self.label_error_text2.set(self.ADMIN_ERROR_TEXT[self.label_error_index2])
        self.label_error = Label(master, textvariable = self.label_error_text2,fg="red")
        
        self.label_username = Label(master,text="Username:")
        self.entry_username = Entry(master)
        
        self.label_password = Label(master,text="Password:")
        self.entry_password = Entry(master,show="*")
        
        self.button_loginSubmit = Button(master,text="Submit",command=lambda:self.errorCheck(username,password))
        
        self.label_divider = Label(master,text="------------")
        
        self.button_saveData = Button(master,text="Save Data",command=lambda:self.saveData(node,filename))
        self.button_quit = Button(master,text="Close App",command=self.close())
        
        self.label_error.grid(row=0, column=0, sticky=W)
        
        self.label_username.grid(row=1, column=0, sticky=W)
        self.entry_username.grid(row=1, column=1, columnspan=2, sticky=W+E)
        
        self.label_password.grid(row=2, column=0, sticky=W)
        self.entry_password.grid(row=2, column=1, columnspan=2, sticky=W+E)
        
        self.button_loginSubmit.grid(row=3,column=1)
        
        self.label_divider.grid(row=4, column=1)
        
        self.button_saveData.grid(row=5,column=1)
        self.button_quit.grid(row=6,column=1)
        
    def errorCheck(self,username,password):
        self.usernameAdmin=self.entry_username.get()
        self.passwordAdmin=self.entry_password.get()
        if self.usernameAdmin != username or self.passwordAdmin != password: 
            print("invalid username or password")
            self.label_error_index2 = 1
            self.label_error_text2.set(self.ADMIN_ERROR_TEXT[self.label_error_index2])
            self.entry_username.delete(0,END)
            self.entry_password.delete(0,END)
        else:
            print("login passed")
            self.login = True
            
    def saveData(self,node,filename):
        if self.login:
            file = open(filename,"w+")
            node.writeToFile(file)
            file.close
        else:
            print("Not logged in")
            self.label_error_index2 = 2
            self.label_error_text2.set(self.ADMIN_ERROR_TEXT[self.label_error_index2])
            
    def close(self):
        if self.login:
            self.master.destroy()
        else:
            print("Not Logged in")

def disable_event():
    pass