import os
import tkinter.font as font
import datetime
import webbrowser
from dotenv import load_dotenv
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from mycontacts import view
from addcontacts import add


## --- INITIALIZE TKINTER ---
root = Tk()
root.title("Tinku's GUI")
root.iconbitmap("./data/icons/contact-book.ico")
root.geometry(os.environ.get("GEOMETRY"))
root.resizable(False, False)


# --- GLOBAL VARIABLES ---
# loading all the variables
load_dotenv()

# get today's date
DATE = datetime.date.today()

# Additional Fonts by Tkinter
TIMES = font.Font(family="Times", size=12)


## --- FUNCTIONS ---
# function to call webpage link
def open_link():
    set_btn["state"] = NORMAL
    help_btn["state"] = DISABLED

    link = "https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/contactbook.md"
    webbrowser.open(link, new=2)
    root.iconify()

# opening the view contacts window
def open_view():
    set_btn["state"] = NORMAL
    view_btn["state"] = DISABLED

    view()
    root.iconify()

# opening the add contact window
def open_add():
    add_btn["state"] = DISABLED
    set_btn["state"] = NORMAL

    add()
    root.iconify()

def set_btns():
    qns =messagebox.askquestion("Warning", "Do you wanna enable the buttons?", icon="warning")

    if qns == "yes":
        add_btn["state"] = NORMAL
        view_btn["state"] = NORMAL
        help_btn["state"] = NORMAL

        set_btn["state"] = DISABLED

## --- MAIN WINDOW ---
# Create Main Frames
header = Frame(root, height=150, bg="white")
header.pack(fill=X)
base = Frame(root, height=500, bg=os.environ.get("BRIGHT_LAV"))
base.pack(fill=X)

# Designing Header Frame
img = Image.open("./data/icons/phone-book.png")
width, height = img.size
img = img.resize((width//8, height//8), Image.ANTIALIAS)
photoimg = ImageTk.PhotoImage(img)
img_lbl = Label(header, image=photoimg, bg="white")
img_lbl.place(x=100, y=40)

heading = Label(header, text="My Contact Book", font=os.environ.get("HELVI21"),
                bg="White", fg=os.environ.get("PEACH"))
heading.place(x=200, y=70)
date = Label(header, text="Date: " + str(DATE),font=os.environ.get("ARIAL12"),
             bg="White", fg=os.environ.get("PEACH"))
date.place(x=530, y=120)

# Designing Base Frame
view_btn = Button(base, fg=os.environ.get("PEACH"), activebackground=os.environ.get("LAVENDER"),
                  text="View Contacts", font=TIMES, padx=7, pady=7, command=open_view)
add_btn  = Button(base, fg=os.environ.get("PEACH"), activebackground=os.environ.get("LAVENDER"),
                  text="Add Contact", font=TIMES, padx=9, pady=7, command=open_add)
help_btn = Button(base, fg=os.environ.get("PEACH"), activebackground=os.environ.get("LAVENDER"),
                  text="Help ?", font=TIMES, padx=30, pady=7, command=open_link)
set_btn = Button(base, fg=os.environ.get("PEACH"), activebackground=os.environ.get("LAVENDER"),
                  text="Reset", font=TIMES, padx=20, pady=5, command=set_btns)

view_btn.place(x=260, y=80)
add_btn.place(x=260, y=150)
help_btn.place(x=260, y=220)
set_btn.place(x=520, y=330)


root.mainloop()
