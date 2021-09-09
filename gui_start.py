from Node import Node
from Person import Person
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk
from gui_main import gui_main

class gui_start:
    def __init__(self,master,node,screenDimStr):
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
        self.button_nFile = Button(self.frame_left,text="Create New",command=lambda:self.createNewFile(node,screenDimStr))

        self.button_oFile = Button(self.frame_right,text="Open existing file",command=lambda:self.openFile(node,screenDimStr))

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

    def createNewFile(self,node,screenDimStr):
        self.filename=self.entry_nFile.get()
        self.filename=self.filename+'.csv'

        self.startMain(node,self.filename,screenDimStr)
        
    def openFile(self,node,screenDimStr):
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

        self.startMain(node,self.filename,screenDimStr)
        

    def startMain(self,node,filename,screenDimStr):
        username = self.entry_username.get()
        password = self.entry_password.get()
        print(username+" "+password)

        mainInterface=Toplevel()
        mainInterface.geometry(screenDimStr)
        mainInterface.overrideredirect(True)
        mainInterface.protocol("WM_DELETE_WINDOW", disable_event)
        mainInterface.configure(bg="black")

        my_gui_main = gui_main(mainInterface,node,filename,username,password)

        mainInterface.bind('<Return>',lambda event: my_gui_main.addItem(node,filename))
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