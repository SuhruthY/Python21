from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
import sqlite3


# --- GLOBAL VARIABLES ---
# get today's date
DATE = datetime.date.today()

# Colors Hex values
LAVENDER = "#E6E6FA"
PEACH = "#FD7272"

# Header Fonts
HELVI21 = "Helvitica 21 bold"
ARIAL12 = "arial 10 bold"

conn = sqlite3.connect("mycontacts.db")
cur = conn.cursor()


# Add Function
# a function to add new contacts
def add():

    global f_name_ntry
    global l_name_ntry
    global ph_no_ntry
    global email_ntry
    global address_ntry

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
    img = Image.open("add-user.png")
    width, height = img.size
    img = img.resize((width // 8, height // 8), Image.ANTIALIAS)
    photoimg = ImageTk.PhotoImage(img)
    img_lbl = Label(header, image=photoimg, bg="white")
    img_lbl.image = photoimg
    img_lbl.place(x=120, y=15)

    heading = Label(header, text="Add New Contact", font=HELVI21,
                    bg="White", fg=PEACH)
    heading.place(x=200, y=40)
    date = Label(header, text="Date: " + str(DATE), font=ARIAL12,
                 bg="White", fg=PEACH)
    date.place(x=530, y=70)

    # Designing Base Frame
    # Creating required labels
    f_name_lbl = Label(base, text="First Name:", font=ARIAL12, bg=LAVENDER)
    l_name_lbl = Label(base, text="Last Name:", font=ARIAL12, bg=LAVENDER)
    ph_no_lbl = Label(base, text="Phone Number:", font=ARIAL12, bg=LAVENDER)
    email_lbl = Label(base, text="Email Address:", font=ARIAL12, bg=LAVENDER)
    address_lbl = Label(base, text="Address:", font=ARIAL12, bg=LAVENDER)

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

    add_prsn_btn = Button(base, text="Add Contact", width=12, font=ARIAL12,
                          command=add_contact)
    add_prsn_btn.place(x=150, y=400)

# Add contact function
# Add the data to database
def add_contact():
    global f_name_ntry
    global l_name_ntry
    global ph_no_ntry
    global email_ntry
    global address_ntry

    first_name = f_name_ntry.get()
    last_name =  l_name_ntry.get()
    phone_no = ph_no_ntry.get()
    email_ID = email_ntry.get()
    address = address_ntry.get(1.0, "end-1c")

    if first_name and last_name and phone_no and email_ID and address:
        try:
            cur.execute(""" insert into 'People' (First_Name, Last_Name, Phone_no, Email_ID, Address)
                        values (?, ?, ?, ?,?)""", (first_name, last_name, phone_no, email_ID, address))
            conn.commit()
            messagebox.showinfo("Sucess", "Contact added")
        except Exception as ex:
            messagebox.showerror("Error", str(e))

    else:
        messagebox.showerror("Error", "Fill all the fields", icon="warning")









