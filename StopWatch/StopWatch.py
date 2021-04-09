from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
import requests, time, io


# --- Global vars ---
HELVI21 =  ("Helvitica", 21, "bold")
ARIAL18 =  ("Arial", 18)
minutes, seconds = 0, 0


# --- FUNCTIONS ---
def center(win):

    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def update():
    global minutes, seconds, run
    btn3["state"] = "normal"
    btn2["state"] = "normal"
    btn["state"] = "disabled"

    if seconds < 59:
        seconds += 1
    elif seconds == 59:
        seconds = 0
        minutes +=1

    # Update Label.
    time_string = "{:02d}:{:02d}".format(minutes, seconds)
    txt.set(time_string)
    stopwatch.config(text=txt.get())
    run = root.after(1000, update)

def stop():
    global run, top, minutes, seconds
    btn3["state"] = "disabled"
    btn2["state"] = "disabled"
    btn["state"] = "normal"

    minutes, seconds = 0, 0

    txt.set("00:00")
    stopwatch.config(text=txt.get())

    btn3["command"] = stamp
    top.destroy()

    root.after_cancel(run)

def add():
    global lstbx, num

    num += 1
    lstbx.insert("end", f"{num}. {txt.get()}")

def stamp():
    global lstbx, top, num
    btn3["command"] = add

    top = tk.Toplevel(root)
    top.geometry("250x250")
    top.resizable(width=0, height=0)
    top.title("WhY GUI | Time Stamps")

    boxtitle = tk.Label(top, text="Time Stamps", pady=5)
    boxtitle.pack()

    frame = tk.Frame(top)
    frame.pack()

    lstbx = tk.Listbox(frame, width=15, height=10,)
    lstbx.pack(side="left", fill="y")

    scroll = tk.Scrollbar(frame, orient="vertical")
    scroll.pack(side="right", fill="y")

    lstbx.config(yscrollcommand=scroll.set)
    scroll.config(command=lstbx.yview)

    num = 1
    lstbx.insert("end", f"{num}. {txt.get()}")

    top.mainloop()


# creating Tk window
root = tk.Tk()

# setting geometry of tk window
root.geometry("400x400")
root.resizable(width=0, height=0)
root.title("WhY GUI")

# setting the favicon
url = "https://raw.githubusercontent.com/SuhruthY/whyfavicon/master/favicon/favicon.ico"
res = requests.get(url)

image_bytes = io.BytesIO(res.content)
image = Image.open(image_bytes)
icon = ImageTk.PhotoImage(image)
root.iconphoto(True, icon)

center(root)

apptitle = tk.Label(root, text="Stop Watch", font=HELVI21, fg="black")
apptitle.pack(pady=25)

# Stopwatch label
txt = tk.StringVar()
txt.set("00:00")

stopwatch = tk.Label(root, text=txt.get(), font=ARIAL18)
stopwatch.pack()

btn = tk.Button(root, text="Start", bd=3, padx=5, pady=5, command=update)
btn2 = tk.Button(root, text="Stop", bd=3, padx=5, pady=5, command=stop, state="disabled")
btn3 = tk.Button(root, text="Add Time Stamp", bd=3, padx=5, pady=5, command=stamp, state="disabled")

btn.place(x=140, y=150)
btn2.place(x=220, y=150)
btn3.place(x=150, y=200)


root.mainloop()