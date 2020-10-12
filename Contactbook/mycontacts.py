from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import datetime

# --- INITAILIZE DATABASE ---
# connect to database
conn = sqlite3.connect("mycontacts.db")
cur = conn.cursor()

# create a table
cur.executescript(""" 
CREATE TABLE IF NOT EXISTS People(
            person_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            ph_no INTEGER,
            email TEXT,
            address_id INTEGER,
            FOREIGN KEY (address_id) 
                REFERENCES Address(address_id)
            );
            
CREATE TABLE IF NOT EXISTS Address(
            address_id INTEGER PRIMARY KEY,
            house_no TEXT,
            street TEXT,
            city TEXT,
            country TEXT,
            zipcode TEXT
            );
            """)

# closing database
conn.commit()
conn.close()


# --- GLOBAL VARIABLES ---
# get today's date
DATE = datetime.date.today()

# Colors Hex values
LAVENDER = "#E6E6FA"
PEACH = "#FD7272"

# Header Fonts
HELVI21 = "Helvitica 21 bold"
ARIAL12 = "arial 10 bold"


def show():
    global my_cntct

    # connect to database
    conn = sqlite3.connect("mycontacts.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM Address")
    crnt_recs = cur.fetchall()

    cur.execute("SELECT * FROM People")
    crnt_ppls = cur.fetchall()

    # closing database
    conn.commit()
    conn.close()


# View Function
# a function to view all contacts
def view():
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



    #show_btn = Button(my_cntct, text="Show Record", command=show)
    #show_btn.place(x=250, y=150)

    #exit_btn = Button(my_cntct, text="Main Menu", command=my_cntct.destroy)
    #exit_btn.place(x=250, y=100)