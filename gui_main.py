from Node import Node
from Person import Person
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk
from gui_admin import gui_admin

class gui_main:
    ERROR_TEXT = [
        " ",
        "Error! Invalid e-mail address",
        "Error! Not a UMBC e-mail address",
    ]
    def __init__(self, master,node,filename,username,password):
        self.master = master
        
        master.title("Jujitsu Club Sign-Up: Involvment Fest")
        
        self.arrowPointer = 0
        
        self.header_font = Font(family = "Arial", size = 30)
        self.main_font = Font(family = "Arial",size = 15)
        self.warning_font = Font(family="Verdana",size = 10)
        self.footer_font = Font(family = "Verdana",size = 10)
        
        self.frame_Left = Frame(master, bg='#f8bf12', width=400, height=900)
        self.frame_center = Frame(master, bg='black', width=800, height=900)
        self.frame_Right = Frame(master, bg='#f8bf12', width=400, height=900)
        
        self.frame_center_top=Frame(self.frame_center,bg="yellow",width=800,height=450)
        self.frame_center_bottom=Frame(self.frame_center,bg="black",width=800,height=450)
        
        image1 = Image.open("logo-retriever1.jpg")
        photo1 = ImageTk.PhotoImage(image1)
        
        self.label_image = Label(self.frame_center_top,image=photo1,borderwidth = 0, highlightthickness=0)
        self.label_image.image = photo1
        
        self.label_header = Label(self.frame_center_bottom, text="        Please enter information below",font = self.header_font,bg="black",fg="#f8bf12")
        
        self.label_fname = Label(self.frame_center_bottom,text="First Name:",font= self.main_font,bg="black",fg="#f8bf12")
        self.entry_fname = Entry(self.frame_center_bottom)
        
        self.label_lname = Label(self.frame_center_bottom,text="Last Name:",font = self.main_font,bg="black",fg="#f8bf12")
        self.entry_lname = Entry(self.frame_center_bottom)
        
        self.label_error_index = 0
        self.label_error_text = StringVar()
        self.label_error_text.set(self.ERROR_TEXT[self.label_error_index])
        self.label_error_email = Label(self.frame_center_bottom, textvariable = self.label_error_text,font=self.warning_font,fg="red",bg="black")
        
        self.label_email = Label(self.frame_center_bottom,text="UMBC Email Address*:",font = self.main_font,bg="black",fg="#f8bf12")
        self.entry_email = Entry(self.frame_center_bottom)
        
        self.label_footer = Label(self.frame_center_bottom, text = " * required field",font = self.footer_font,bg="black",fg="#f8bf12")

        self.submit_button = Button(self.frame_center_bottom, text="Submit",bg="black",fg="#f8bf12", command=lambda: self.addItem(node,filename))
        
        self.button_adminOptions = Button(self.frame_center_bottom,text = "Admin Options",bg="black",fg="#f8bf12",command=lambda: self.adminWindow(node,username,password,filename))

        # LAYOUT
        self.frame_Left.grid(row=0,column= 0,sticky=N+S)
        self.frame_center.grid(row=0,column =1,sticky=N+S+E+W)
        self.frame_Right.grid(row=0,column=2,sticky=N+S)
        
        self.frame_center_top.grid(row=0,column = 0, sticky = N)
        self.frame_center_bottom.grid(row=1,column=0,sticky = S)
        
        self.label_image.place(x=0,y=0,bordermode=OUTSIDE)
        
        
        self.label_header.grid(row=0,column=0,columnspan=6, sticky=W+S)
        
        self.label_fname.grid(row=1, column=1, sticky=E)
        self.entry_fname.grid(row=1, column=2, columnspan=3, sticky=W+E)
        
        self.label_lname.grid(row=2, column=1, sticky=E)
        self.entry_lname.grid(row=2, column=2, columnspan=3, sticky=W+E)
        
        self.label_error_email.grid(row=3, column=1, sticky=E)
        
        self.label_email.grid(row=4, column=1, sticky=E)
        self.entry_email.grid(row=4, column=2, columnspan=3, sticky=W+E)

        self.label_footer.grid(row=5, column=1, sticky=W)
        
        self.submit_button.grid(row=6, column=2)
        self.button_adminOptions.grid(row=6,column=6,sticky=E)
        

    def addItem(self, node,filename):
        fName = self.entry_fname.get()
        lName = self.entry_lname.get()
        email = self.entry_email.get()
        if '@' not in email:
            print("@ not present")
            self.label_error_index = 1
            self.label_error_text.set(self.ERROR_TEXT[self.label_error_index])
        else:
            index = email.find('umbc.edu')
            if index == -1:
                print(".edu not present")
                self.label_error_index = 2
                self.label_error_text.set(self.ERROR_TEXT[self.label_error_index])
            else:
                self.label_error_index = 0
                self.label_error_text.set(self.ERROR_TEXT[self.label_error_index])
                p = Person(fName,lName,email)
                node.insert(p)
                print("data added")
                file = open(filename,"w+")
                node.writeToFile(file)
                file.close
                print("data saved")
                self.entry_lname.delete(0,END)
                self.entry_fname.delete(0,END)
                self.entry_email.delete(0,END)
                self.entry_fname.focus_set()
        
    def adminWindow(self,node,username,password,filename):
        adminLoginInterface =Toplevel()
        my_gui_admin = gui_admin(adminLoginInterface,node,username,password,filename)
        
    def arrowControls(self,pointerCount,direction):
        pointerCount = (pointerCount + direction) % 3
        self.arrowPointer = pointerCount
        if pointerCount==0:
            self.entry_fname.focus_set()
        if pointerCount==1:
            self.entry_lname.focus_set()
        if pointerCount==2:
            self.entry_email.focus_set()

def disable_event():
    pass