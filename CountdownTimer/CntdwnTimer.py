from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
import requests, time, io

# --- Global vars ---
HELVI21 =  ("Helvitica", 21, "bold")
ARIAL18 =  ("Arial", 18)


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

def pause():
    global  btn2click
    btn2click = True

    btn["state"] = "normal"
    btn2["state"] = "disabled"
    btn3["state"] = "normal"

def stop():
    global  btn3click
    btn3click = True

    btn["state"] = "normal"
    btn2["state"] = "disabled"
    btn3["state"] = "disabled"

def update():
    btn["state"] = "disabled"
    btn2["state"] = "normal"
    btn3["state"] = "normal"

    global btn2click, btn3click
    btn2click, btn3click = False, False

    tmp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

    while tmp > -1:
        if btn3click == True:
            reset()
            break

        if btn2click == True:
            time.sleep(10)

            qn = messagebox.askquestion(title="confirm", message="Do you wanna continue?")

            if qn == "no":
                reset()
                break
            else:
                btn2click = False
                btn["state"] =  "disabled"
                btn2["state"] =  "normal"
                btn3["state"] =  "normal"

        mins, secs = divmod(tmp, 60)
        hours = 0

        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if (tmp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")

        tmp -= 1

def reset(HRS="00", MIN="00" ,SEC="00"):
    hour.set(HRS)
    minute.set(SEC)
    second.set(MIN)

def submit():
    letsupdate =  False

    try:
        HRS, MIN, SEC = int(hour.get()), int(minute.get()), int(second.get())

        if HRS == 0 and MIN == 0 and SEC == 0:
            messagebox.showinfo(title="No input", message="Enter some input to before starting the timer")
            return
        letsupdate = True
    except:
        messagebox.showerror(title="Wrong Input", message="Please enter only integers")
        reset()

    if MIN > 60 or SEC > 60:
        messagebox.showerror(title="Wrong Input", message="Minutes and seconds cant exceed 60")
        letsupdate = False
        reset()
    elif HRS > 12:
        messagebox.showwarning(title="Warning", message="Setting hours more than 12 will run too long!")
        letsupdate = True

    if letsupdate: update()


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
root.iconphoto(False, icon)

center(root)


apptitle = tk.Label(root, text="Countdown Timer", font=HELVI21, fg="black")
apptitle.pack(pady=25)

# defining variables
hour, minute, second  = tk.StringVar(), tk.StringVar(), tk.StringVar()

# setting the defaults
hour.set("00")
minute.set("00")
second.set("00")

# taking user inputs
hourEntry = tk.Entry(root, width=3, font=ARIAL18,textvariable=hour)
minuteEntry = tk.Entry(root, width=3, font=ARIAL18, textvariable=minute)
secondEntry = tk.Entry(root, width=3, font=ARIAL18, textvariable=second)

hourEntry.place(x=130, y=120)
minuteEntry.place(x=180, y=120)
secondEntry.place(x=230, y=120)


# button widget
btn = tk.Button(root, text='Start', bd='3', pady=5, padx=5, command=submit)
btn2 = tk.Button(root, text='Pause', bd='3', pady=5, padx=5, command=pause, state="disabled")
btn3 = tk.Button(root, text='Stop', bd='3', pady=5, padx=5, command=stop, state="disabled")

btn.place(x=180, y=170)
btn2.place(x=150, y=220)
btn3.place(x=210, y=220)

root.mainloop()
