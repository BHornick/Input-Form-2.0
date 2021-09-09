from Node import Node
from Person import Person
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk
from gui_start import gui_start

def disable_event():
    pass

root = Node()   
interface = Tk()
screenX=str(interface.winfo_screenwidth())
screenY=str(interface.winfo_screenheight())
screenDimStr=screenX+"x"+screenY
interface.geometry("400x150")
interface.resizable(False, False)
my_gui = gui_start(interface,root,screenDimStr)

interface.bind('<Up>',lambda event: my_gui.arrowControls(my_gui.arrowPointer, -1))
interface.bind('<Down>',lambda event: my_gui.arrowControls(my_gui.arrowPointer, 1))
interface.bind('<Tab>',lambda event: my_gui.arrowControls(my_gui.arrowPointer, 1))

interface.mainloop()
