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

class gui_start:
    def __init__(self,master,node):
        self.master=master
        master.title("Input Form-Startup")

        self.arrowPointer = 0

        self.frame_top = Frame(master,width=400,height=50,padx=65)
        self.frame_dividerTop = Frame(master,bg="black",width=380,height=2)
        self.frame_left = Frame(master,width=200,height=100,padx=2,pady=10)
        self.frame_right = Frame(master,width=200,height=100,padx=2,pady=10)
        self.frame_dividerMiddle = Frame(master,bg="black",width=2,height=65)

        self.label_username = Label(self.frame_top,text="Create Session Username:")
        self.entry_username = Entry(self.frame_top)

        self.label_password = Label(self.frame_top,text="Create Session Password:")
        self.entry_password = Entry(self.frame_top,show="*")

        self.label_instructions = Label(self.frame_top,text="Create new file or select existing .csv")

        self.label_nFile = Label(self.frame_left,text="File Name:")
        self.entry_nFile = Entry(self.frame_left,width=12)
        self.button_nFile = Button(self.frame_left,text="Create New",command=lambda:self.createNewFile(node))

        self.button_oFile = Button(self.frame_right,text="Open existing file",command=lambda:self.openFile(node))

#LAYOUT
        self.frame_top.grid(row=0,column=0,sticky=E+W,columnspan=3)
        self.frame_dividerTop.grid(row=1,column=0,sticky=N,columnspan=3)
        self.frame_left.grid(row=2,column=0,sticky=N+E+S+W)
        self.frame_dividerMiddle.grid(row=2,column=1)
        self.frame_right.grid(row=2,column=2,sticky=N+S+W+E)

        self.label_username.grid(row=0,column=0,sticky=E)
        self.entry_username.grid(row=0,column=1,columnspan=2,sticky=E)
        
        self.label_password.grid(row=1,column=0,sticky=E)
        self.entry_password.grid(row=1,column=1,columnspan=2,sticky=E)

        self.label_instructions.grid(row=3,column=0,columnspan=2,padx=0)

        self.label_nFile.grid(row=0,column=0,sticky=W)
        self.entry_nFile.grid(row=0,column=1,sticky=W)
        self.button_nFile.grid(row=2,column=1,sticky=W,columnspan=2)

        self.button_oFile.grid(row=0,column=0)

        self.entry_username.focus_set()

    def createNewFile(self,node):
        self.filename=self.entry_nFile.get()
        self.filename=self.filename+'.csv'

        self.startMain(node,self.filename)
        
    def openFile(self,node):
        self.filename = filedialog.askopenfilename()
        self.validFile = False
        while(self.validFile==False):
            if(self.filename.find('.csv')==-1):
               self.filename = filedialog.askopenfilename()
            else:
                self.validFile = True 
        self.file = open(self.filename,"r")
        for line in self.file:
            segment = line.split(",")
            fName = segment[0]
            lName = segment[1]
            email = segment[2]
            p = Person(fName,lName,email)
            node.insert(p)

        self.startMain(node,self.filename)
        

    def startMain(self,node,filename):
        username = self.entry_username.get()
        password = self.entry_password.get()
        print(username+" "+password)

        mainInterface=Toplevel()
        mainInterface.geometry(screenDimStr)
        mainInterface.overrideredirect(True)
        mainInterface.protocol("WM_DELETE_WINDOW", disable_event)
        mainInterface.configure(bg="black")

        my_gui_main = gui_main(mainInterface,node,filename,username,password)

        mainInterface.bind('<Return>',lambda event: my_gui_main.addItem(root,filename))
        mainInterface.bind('<Up>',lambda event: my_gui_main.arrowControls(my_gui_main.arrowPointer, -1))
        mainInterface.bind('<Down>',lambda event: my_gui_main.arrowControls(my_gui_main.arrowPointer, 1))
        mainInterface.bind('<Tab>',lambda event: my_gui_main.arrowControls(my_gui_main.arrowPointer, 1))

        my_gui_main.entry_fname.focus_set()
        self.master.withdraw()

    def arrowControls(self,pointerCount,direction):
        pointerCount = (pointerCount + direction) % 3
        self.arrowPointer = pointerCount
        if pointerCount==0:
            self.entry_username.focus_set()
        if pointerCount==1:
            self.entry_password.focus_set()
        if pointerCount==2:
            self.entry_nFile.focus_set()

def disable_event():
    pass

root = Node()   
interface = Tk()
screenX=str(interface.winfo_screenwidth())
screenY=str(interface.winfo_screenheight())
screenDimStr=screenX+"x"+screenY
interface.geometry("400x150")
interface.resizable(False, False)
my_gui = gui_start(interface,root)

interface.bind('<Up>',lambda event: my_gui.arrowControls(my_gui.arrowPointer, -1))
interface.bind('<Down>',lambda event: my_gui.arrowControls(my_gui.arrowPointer, 1))
interface.bind('<Tab>',lambda event: my_gui.arrowControls(my_gui.arrowPointer, 1))

interface.mainloop()
