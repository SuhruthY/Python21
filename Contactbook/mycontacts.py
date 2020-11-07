from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import datetime
from addcontacts import add

# --- INITAILIZE DATABASE ---
# connect to database
conn = sqlite3.connect("mycontacts.db")
cur = conn.cursor()

# create a table
cur.executescript(""" 
CREATE TABLE IF NOT EXISTS People(
            Person_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            First_Name TEXT,
            Last_Name TEXT,
            Phone_no INTEGER,
            Email_ID TEXT,
            Address TEXT
            )""")

# closing database
conn.commit()


# --- GLOBAL VARIABLES ---
# get today's date
DATE = datetime.date.today()

# Colors Hex values
LAVENDER = "#E6E6FA"
PEACH = "#FD7272"

# Header Fonts
HELVI21 = "Helvitica 21 bold"
ARIAL12 = "arial 10 bold"


## --- Functions ---
# Open Add function
def open_add():
    global my_cntct

    my_cntct.destroy()
    add()

# View Function
# a function to view all contacts
def view():
    global my_cntct

    my_cntct = Toplevel()
    my_cntct.title("My Contacts Book")
    my_cntct.iconbitmap("contact-book.ico")
    my_cntct.geometry("650x550+350+250")
    my_cntct.resizable(False, False)

    # Create Main Frames
    header = Frame(my_cntct, height=100, bg="white")
    header.pack(fill=X)
    base = Frame(my_cntct, height=550, bg=LAVENDER)
    base.pack(fill=X)

    # Designing Header Frame
    img = Image.open("list.png")
    width, height = img.size
    img = img.resize((width // 8, height // 8), Image.ANTIALIAS)
    photoimg = ImageTk.PhotoImage(img)
    img_lbl = Label(header, image=photoimg, bg="white")
    img_lbl.image = photoimg
    img_lbl.place(x=120, y=15)

    heading = Label(header, text="My Contacts", font=HELVI21,
                    bg="White", fg=PEACH)
    heading.place(x=200, y=40)
    date = Label(header, text="Date: " + str(DATE), font=ARIAL12,
                 bg="White", fg=PEACH)
    date.place(x=530, y=70)

    # Designing Base
    lst_box = Listbox(base, width=60, height=26)
    lst_box.grid(row=0, column=0, padx=10, pady=10)
    # create a scroll bar
    scrl_bar = Scrollbar(base, orient=VERTICAL)
    scrl_bar.grid(row=0, column=1, sticky=N+S)
    # set scroll bar
    lst_box.config(yscrollcommand=scrl_bar.set)
    scrl_bar.config(command=lst_box.yview)

    # Creating Buttons
    add_btn = Button(base, text="Add", width=12, font=ARIAL12, command=open_add)
    updt_btn = Button(base, text="Update", width=12, font=ARIAL12)
    dsply_btn = Button(base, text="Display", width=12, font=ARIAL12)
    del_btn = Button(base, text="Delete", width=12, font=ARIAL12)

    add_btn.grid(row=0, column=2, padx=20, pady=10, columnspan=2, sticky=N)
    updt_btn.grid(row=0, column=2, padx=20, pady=50, columnspan=2, sticky=N)
    dsply_btn.grid(row=0, column=2, padx=20, pady=90, columnspan=2, sticky=N)
    del_btn.grid(row=0, column=2, padx=20, pady=130, columnspan=2, sticky=N)

    contacts = cur.execute("select * from People").fetchall()

    count = 0
    for contact in contacts:
        lst_box.insert(count, f"{contact[0]}. {contact[1]}{contact[2]}")
        count += 1


