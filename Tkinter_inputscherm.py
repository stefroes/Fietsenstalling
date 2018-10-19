from tkinter import *
from tkinter import messagebox
import db_connect
<<<<<<< HEAD:Tkinter.input.py
from general.general import *

# GLOBALS
db = db_connect.db
white = '#FFFFFF'
blue = '#013174'
yellow = '#F4C03D'
high_dpi = True
fullscreen = True
=======
import re


def login():
    login.grid()

blauw = '#013174'
geel = '#F4C03D'

gui = Tk()
gui.geometry("700x250")
gui.configure(bg=geel)
>>>>>>> origin/master:Tkinter_inputscherm.py


class MainScreen:
    def __init__(self, master):
        self.master = master
        self.photo_label = Label(self.master, image=PhotoImage(file='assets/img/main.png'))


class RegisterScreen:
    def __init__(self, master):
        self.master = master

        self.first_name_label = Label(self.master, width=15, text='Voornaam: ', bg=yellow, fg=blue, padx=10, pady=10).grid(row=0, column=0)
        self.first_name_entry = Entry(self.master, width=30)
        self.first_name_entry.grid(row=0, column=1)

        self.insertion_label = Label(self.master, width=15, text='Tussenvoegsels: ', bg=yellow, fg=blue, padx=10, pady=10).grid(row=1, column=0)
        self.insertion_entry = Entry(self.master, width=30)
        self.insertion_entry.grid(row=1, column=1)

        self.last_name_label = Label(self.master, width=15, text='Achternaam: ', bg=yellow, fg=blue, padx=10, pady=10).grid(row=2, column=0)
        self.last_name_entry = Entry(self.master, width=30)
        self.last_name_entry.grid(row=2, column=1)

        self.zip_label = Label(self.master, width=15, text='Postcode: ', bg=yellow, fg=blue, padx=10, pady=10).grid(row=3, column=0)
        self.zip_entry = Entry(self.master, width=30)
        self.zip_entry.grid(row=3, column=1)

        self.streetnumber_label = Label(self.master, width=15, text='Huisnummer: ', bg=yellow, fg=blue, padx=10, pady=10).grid(row=4, column=0)
        self.streetnumber_entry = Entry(self.master, width=30)
        self.streetnumber_entry.grid(row=4, column=1)

        self.email_label = Label(self.master, width=15, text='E-mail: ', bg=yellow, fg=blue, padx=10, pady=10).grid(row=5, column=0)
        self.email_entry = Entry(self.master, width=30)
        self.email_entry.grid(row=5, column=1)

        self.register_button = Button(self.master, width=15, text='Registreren', highlightbackground=blue, bg=blue, fg=white, command=self.register).grid(row=6, column=0)
        self.close_button = Button(self.master, text='New Window', width=15, command=self.new_window).grid(row=6, column=1)

    def register(self):
        data = ('ABCDE', self.first_name_entry.get(), self.insertion_entry.get(), self.last_name_entry.get(), self.zip_entry.get(), self.streetnumber_entry.get(), self.email_entry.get(), '2018-10-16 12:00:00')

        cursor = db.cursor()
        cursor.execute('INSERT INTO user(unique_code, first_name, insertion, last_name, zip, streetnumber, email, date_time) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', data)
        db.commit()
        print(cursor.rowcount)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Demo2(self.newWindow)


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main():
    root = Tk()

<<<<<<< HEAD:Tkinter.input.py
    if high_dpi:
        root.call('tk', 'scaling', 4)
    root.attributes('-fullscreen', True)
    root.geometry('900x700')
    root.configure(bg=yellow)
    root.title('NS Fietsenstalling')

    main = MainScreen(root)
    register = RegisterScreen(root)
    root.mainloop()
=======
def printIt():
    callback_zip()
    callback_email()
    callback_huisnummer()

# callback functies om te checken of input klopt
def callback_zip():
    zip = var4.get()
    if len(zip) != 6:
        messagebox.showerror("Error", "Vul een geldig postcode in.")
    else:
        print(var4.get())
>>>>>>> origin/master:Tkinter_inputscherm.py

def callback_huisnummer():
    housenumber = var5.get()
    if len(housenumber) > 3 :
        messagebox.showerror("Error", "Vul een geldig huisnummer in.")
    else:
        print(var5.get())

<<<<<<< HEAD:Tkinter.input.py
if __name__ == '__main__':
    main()
=======
def callback_email():
    email = var6.get()
    if re.search(r"[@]", email) is None:
        messagebox.showerror("Error", "Je email mist een '@'.")
    elif re.search(r"[.]", email) is None:
        messagebox.showerror("Error", "Je email mist een '.'.")
    else:
        print(var6.get())

Button(gui, width=15, text="Inloggen" , highlightbackground=blauw, bg=blauw, command=printIt).grid(row=6, column=0)
Button(gui, width=15, text="Registreren" ,highlightbackground=blauw, bg=blauw, command=enter).grid(row=6, column=1)
a = Button(gui, width=15, text="Zip" , highlightbackground=blauw, bg=blauw, command=callback_zip).grid(row=6, column=2)
b = Button(gui, width=15, text="Huisnummer" , highlightbackground=blauw, bg=blauw, command=callback_huisnummer).grid(row=6, column=3)
c = Button(gui, width=15, text="Email" , highlightbackground=blauw, bg=blauw, command=callback_email).grid(row=6, column=4)

gui.mainloop()

# error functie
# import tkinter
# from tkinter import *
# from tkinter import messagebox
#
# # hide main window
# root = tkinter.Tk()
# # root.withdraw()
#
# v = StringVar()
# e = Entry(root, textvariable=v)
# e.pack()
#
# e.focus_set()
#
# def callback():
#     invoer = v.get()
#     if invoer != 'hoi':
#         messagebox.showerror("Error", "Is geen int.")
#     else:
#         print(e.get())
#
# b = Button(root, text="get", width=10, command=callback)
# b.pack()
#
# mainloop()
>>>>>>> origin/master:Tkinter_inputscherm.py
