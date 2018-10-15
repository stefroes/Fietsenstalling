from tkinter import *
import db_connect

def login():
    login.grid()

gui = Tk()
db = db_connect.db

gui.title("Login NS fietsenstalling")

var1 = StringVar()
var2 = StringVar()
username = None               # Global variable declaration
password = None

login = Frame(master=gui)
Label(gui, text="Username: ").grid(row=0, sticky=W)
e1 = Entry(gui, textvariable=var1).grid(row=0, column=1)

Label(gui, text="Password: ").grid(row=1, sticky=W)
e2 = Entry(gui, textvariable=var2).grid(row=1, column=1)

def enter():
    global username, password
    username = var1.get()
    password = var2.get()


def printIt():
    global username, password
    print(username)
    print(password)

    cursor = db.cursor()
    query = "SELECT email FROM user WHERE email = '{}'".format(username)
    print(query)
    cursor.execute(query)
    email = cursor.fetchone()

    goed_email = email[0]

    if username == goed_email:
        eval(input('Wat wil je nu zeggen pik: '))
        print('lekker bezig man')
    else:
        print('Nee man')

Button(gui, width=15, text="ENTER", command=enter).grid(row=0, column=3)
Button(gui, width=15, text="PRINT", command=printIt).grid(row=1, column=3)


gui.mainloop()