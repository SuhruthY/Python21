import os
import tkinter.font as font
import datetime
from dotenv import load_dotenv
from tkinter import *
from PIL import Image,ImageTk
from mycontacts import view
from addcontacts import add

# --- INITIALIZE TKINTER ---
root = Tk()
root.title("Tinku's GUI")
root.iconbitmap("./data/icons/contact-book.ico")
root.geometry("650x550+350+250")
root.resizable(False, False)

# --- GLOBAL VARIABLES ---
# loading all the variables
load_dotenv()

# get today's date
DATE = datetime.date.today()

# Additional Fonts by Tkinter
TIMES = font.Font(family="Times", size=12)


# --- MAIN WINDOW ---
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
                  text="View Contacts", font=TIMES, padx=7, pady=7, command=view)
add_btn  = Button(base, fg=os.environ.get("PEACH"), activebackground=os.environ.get("LAVENDER"),
                  text="Add Contacts", font=TIMES, padx=9, pady=7, command=add)
edit_btn = Button(base, fg=os.environ.get("PEACH"), activebackground=os.environ.get("LAVENDER"),
                  text="Edit Contacts", font=TIMES, padx=10, pady=7)
help_btn = Button(base, fg=os.environ.get("PEACH"), activebackground=os.environ.get("LAVENDER"),
                  text="Help ?", font=TIMES, padx=30, pady=7)

view_btn.place(x=260, y=60)
add_btn.place(x=260, y=120)
edit_btn.place(x=260, y=180)
help_btn.place(x=260, y=240)




root.mainloop()
