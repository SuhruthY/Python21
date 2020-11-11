import os
import datetime
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from dotenv import load_dotenv


## --- Loding the database ---
conn = sqlite3.connect("mycontacts.db")
cur = conn.cursor()


## --- GLOBAL VARIABLES ---
# loading all the variables
load_dotenv()

# get today's date
DATE = datetime.date.today()


## --- FUNCTIONS ---
# Add Function
# a function to add new contacts
def add():
    global add_cntct, f_name_ntry, l_name_ntry, ph_no_ntry, email_ntry, address_ntry

    add_cntct = Toplevel()
    add_cntct.title("My Contacts Book")
    add_cntct.iconbitmap("./data/icons/contact-book.ico")
    add_cntct.geometry(os.environ.get("GEOMETRY"))
    add_cntct.resizable(False, False)

    # Create Main Frames
    header = Frame(add_cntct, height=100, bg="white")
    header.pack(fill=X)
    base = Frame(add_cntct, height=550, bg=os.environ.get("LAVPINK"))
    base.pack(fill=X)

    # Designing Header Frame
    img = Image.open("./data/icons/add-user.png")
    width, height = img.size
    img = img.resize((width // 8, height // 8), Image.ANTIALIAS)
    photoimg = ImageTk.PhotoImage(img)
    img_lbl = Label(header, image=photoimg, bg="white")
    img_lbl.image = photoimg
    img_lbl.place(x=120, y=15)

    heading = Label(header, text="Add New Contact", font=os.environ.get("HELVI21"),
                    bg="White", fg=os.environ.get("PEACH"))
    heading.place(x=200, y=40)
    date = Label(header, text="Date: " + str(DATE), font=os.environ.get("ARIAl12"),
                 bg="White", fg=os.environ.get("PEACH"))
    date.place(x=530, y=70)

    # Designing Base Frame
    # Creating required labels
    f_name_lbl = Label(base, text="First Name:", font=os.environ.get("ARIAL12"), bg=os.environ.get("LAVPINK"))
    l_name_lbl = Label(base, text="Last Name:", font=os.environ.get("ARIAL12"), bg=os.environ.get("LAVPINK"))
    ph_no_lbl = Label(base, text="Phone Number:", font=os.environ.get("ARIAL12"), bg=os.environ.get("LAVPINK"))
    email_lbl = Label(base, text="Email Address:", font=os.environ.get("ARIAL12"), bg=os.environ.get("LAVPINK"))
    address_lbl = Label(base, text="Address:", font=os.environ.get("ARIAL12"), bg=os.environ.get("LAVPINK"))

    f_name_lbl.place(x=40, y=40)
    l_name_lbl.place(x=40, y=80)
    ph_no_lbl.place(x=40, y=120)
    email_lbl.place(x=40, y=160)
    address_lbl.place(x=40,y=200)

    # Creating required entry boxes
    f_name_ntry = Entry(base, width=50, bd=2)
    l_name_ntry = Entry(base, width=50, bd=2)
    ph_no_ntry = Entry(base, width=50, bd=2)
    email_ntry = Entry(base, width=50, bd=2)
    address_ntry = Text(base, width=50, height=10,bd=2)

    f_name_ntry.place(x=150, y=40)
    l_name_ntry.place(x=150, y=80)
    ph_no_ntry.place(x=150, y=120)
    email_ntry.place(x=150, y=160)
    address_ntry.place(x=150, y=200)

    add_prsn_btn = Button(base, text="Add Contact", width=12, font=os.environ.get("ARIAL12"),
                          command=add_contact)
    add_prsn_btn.place(x=150, y=400)

# Add contact function
# Add the data to database
def add_contact():
    global add_cntct, f_name_ntry, l_name_ntry, ph_no_ntry, email_ntry, address_ntry

    first_name,last_name, phone_no, email_ID, address = f_name_ntry.get(), l_name_ntry.get(), ph_no_ntry.get(), email_ntry.get(),address_ntry.get(1.0, "end-1c")

    if first_name and last_name and phone_no and email_ID and address:
        try:
            cur.execute(""" insert into 'People' (First_Name, Last_Name, Phone_no, Email_ID, Address)
                        values (?, ?, ?, ?,?)""", (first_name, last_name, phone_no, email_ID, address))
            conn.commit()
            messagebox.showinfo("Sucess", "Contact added")
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

        add_cntct.destroy()

    else:
        messagebox.showerror("Error", "Fill all the fields", icon="warning")









