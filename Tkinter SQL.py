from tkinter import *
import db_connect

def login():
    login.grid()

gui = Tk()
gui.geometry("300x100")
db = db_connect.db

gui.title("Login NS fietsenstalling")

var1 = StringVar()
# var2 = StringVar()
username = None               # Global variable declaration
# password = None

login = Frame(master=gui)
Label(gui, width=15, text="Email: ").grid(row=0, column=0)
e1 = Entry(gui, width=29, textvariable=var1).grid(row=0, column=1)

# Label(gui, text="Password: ").grid(row=1, sticky=W)
# e2 = Entry(gui, textvariable=var2).grid(row=1, column=1)

def enter():
    global username, password
    username = var1.get()
    # password = var2.get()

    print(username)
    # print(password)

    cursor = db.cursor()
    query = "SELECT email FROM user WHERE email = '{}'".format(username)
    cursor.execute(query)
    email = cursor.fetchone()

    goed_email = email[0]

    if username == goed_email:
        print('lekker bezig man')
    else:
        print('De ingevoerde gegevens kloppen niet.')

def printIt():
    print('Kan ff niet nu')

Button(gui, width=15, text="Inloggen", command=enter).grid(row=3, column=0)
Button(gui, width=15, text="Registreren", command=printIt).grid(row=3, column=1)


gui.mainloop()