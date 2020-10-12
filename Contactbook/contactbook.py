from tkinter import *
from PIL import Image,ImageTk
import tkinter.font as font
import datetime
from mycontacts import view


# --- INITIALIZE TKINTER ---
root = Tk()
root.title("Tinku's GUI")
root.iconbitmap("contact-book.ico")
root.geometry("650x550+350+250")
root.resizable(False, False)

# --- GLOBAL VARIABLES ---
# get today's date
DATE = datetime.date.today()

# Color Hex values
LAVENDER = "#82589F"
PURPLE = "#b19cd9"
PEACH = "#FD7272"

# Header Fonts
HELVI21 = "Helvitica 21 bold"
ARIAL12 = "arial 10 bold"

# Additional Fonts by Tkinter
TIMES = font.Font(family="Times", size=12)


# --- All Functions ---


# --- MAIN WINDOW ---
# Create Main Frames
header = Frame(root, height=150, bg="white")
header.pack(fill=X)
base = Frame(root, height=500, bg=PURPLE)
base.pack(fill=X)

# Designing Header Frame
img = Image.open("phone-book.png")
width, height = img.size
img = img.resize((width//8, height//8), Image.ANTIALIAS)
photoimg = ImageTk.PhotoImage(img)
img_lbl = Label(header, image=photoimg, bg="white")
img_lbl.place(x=100, y=40)

heading = Label(header, text="My Contact Book", font=HELVI21,
                bg="White", fg=PEACH)
heading.place(x=200, y=70)
date = Label(header, text="Date: " + str(DATE),font=ARIAL12,
             bg="White", fg=PEACH)
date.place(x=530, y=120)

# Designing Base Frame
view_btn = Button(base, text="View Contacts", fg=PEACH, activebackground=LAVENDER,
                  font=TIMES, padx=7, pady=7, command=view)
add_btn  = Button(base, text="Add Contacts",  fg=PEACH, activebackground=LAVENDER, font=TIMES, padx=9, pady=7)
edit_btn = Button(base, text="Edit Contacts",  fg=PEACH, activebackground=LAVENDER, font=TIMES, padx=10, pady=7)
help_btn = Button(base, text="Help ?",  fg=PEACH, activebackground=LAVENDER, font=TIMES, padx=30, pady=7)

view_btn.place(x=260, y=60)
add_btn.place(x=260, y=120)
edit_btn.place(x=260, y=180)
help_btn.place(x=260, y=240)




root.mainloop()
