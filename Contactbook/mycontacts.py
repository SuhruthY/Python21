import os
import sqlite3
import datetime
from dotenv import load_dotenv
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from addcontacts import add
from updatecontacts import update
from displaycontacts import display

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
# loading all the variables
load_dotenv()

# get today's date
DATE = datetime.date.today()


## --- FUNCTIONS ---
# Open Add Function
def open_add():
    global my_cntct
    my_cntct.destroy()
    add()

# Open Update Function
def open_update():
    global lst_box

    try:
        index = lst_box.curselection()
        user_id = lst_box.get(index).split()[0]
        update(user_id)
    except Exception as ex:
        messagebox.showerror('Error', str(ex), icon="warning")

# Open Display Function
def open_display():
    global lst_box

    try:
        index = lst_box.curselection()
        user_id = lst_box.get(index).split()[0]
        display(user_id)
    except Exception as ex:
        messagebox.showerror('Error', str(ex), icon="warning")

# function to delete a contact
def delete_contact():
    global my_cntct
    global lst_box

    try:
        index = lst_box.curselection()
        user_id = lst_box.get(index).split()[0]

        ans = messagebox.askquestion("Warning", f"are you sure, you wanna delete '{lst_box.get(index).split()[1]}' ?")

        if ans == "yes":
            try:
                cur.execute(f" delete from People where Person_ID = {user_id}")
                conn.commit()
                messagebox.showinfo("Sucess", "Contact Deleted")
                my_cntct.destroy()
            except Exception as ex:
                messagebox.showinfo("Info", str(ex))

    except Exception as ex:
        messagebox.showinfo("Info", str(ex))


# View Function
# a function to view all contacts
def view():
    global my_cntct, lst_box

    my_cntct = Toplevel()
    my_cntct.title("My Contacts Book")
    my_cntct.iconbitmap("./data/icons/contact-book.ico")
    my_cntct.geometry("650x550+350+250")
    my_cntct.resizable(False, False)

    # Create Main Frames
    header = Frame(my_cntct, height=100, bg="white")
    header.pack(fill=X)
    base = Frame(my_cntct, height=550, bg=os.environ.get("MED_LAVMAGENTA"))
    base.pack(fill=X)

    # Designing Header Frame
    img = Image.open("./data/icons/list.png")
    width, height = img.size
    img = img.resize((width // 8, height // 8), Image.ANTIALIAS)
    photoimg = ImageTk.PhotoImage(img)
    img_lbl = Label(header, image=photoimg, bg="white")
    img_lbl.image = photoimg
    img_lbl.place(x=120, y=15)

    heading = Label(header, text="My Contacts", font=os.environ.get("HELVI21"),
                    bg="White", fg=os.environ.get("PEACH"))
    heading.place(x=200, y=40)
    date = Label(header, text="Date: " + str(DATE), font=os.environ.get("ARIAL 12"),
                 bg="White", fg=os.environ.get("PEACH"))
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
    add_btn = Button(base, text="Add", width=12, font=os.environ.get("ARIAL12"), command=open_add)
    updt_btn = Button(base, text="Update", width=12, font=os.environ.get("ARIAL12"), command=open_update)
    dsply_btn = Button(base, text="Display", width=12, font=os.environ.get("ARIAL12"), command=open_display)
    del_btn = Button(base, text="Delete", width=12, font=os.environ.get("ARIAL12"), command=delete_contact)

    add_btn.grid(row=0, column=2, padx=20, pady=10, columnspan=2, sticky=N)
    updt_btn.grid(row=0, column=2, padx=20, pady=50, columnspan=2, sticky=N)
    dsply_btn.grid(row=0, column=2, padx=20, pady=90, columnspan=2, sticky=N)
    del_btn.grid(row=0, column=2, padx=20, pady=130, columnspan=2, sticky=N)

    contacts = cur.execute("select * from People").fetchall()

    count = 0
    for contact in contacts:
        lst_box.insert(count, f"{contact[0]}. {contact[1]}{contact[2]}")
        count += 1


