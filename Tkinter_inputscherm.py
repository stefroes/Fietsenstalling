from tkinter import *
import db_connect

def login():
    login.grid()

blauw = '#013174'
geel = '#F4C03D'

gui = Tk()
gui.geometry("700x650")
gui.configure(bg=geel)



db = db_connect.db

gui.title("Login NS fietsenstalling")

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
# var2 = StringVar()
username = None               # Global variable declaration
# password = None

login = Frame(master=gui)
Label(gui, width=15, text="Voornaam: ", bg=geel, fg=blauw).grid(row=0, column=0)
first_name_entry = Entry(gui, width=29, textvariable=var1).grid(row=0, column=1)

Label(gui, width=15, text="Tussenvoegsels: ", bg=geel, fg=blauw).grid(row=1, column=0)
insertion_entry = Entry(gui, width=29, textvariable=var2).grid(row=1, column=1)

Label(gui, width=15, text="Achternaam: ", bg=geel, fg=blauw).grid(row=2, column=0)
last_name_entry = Entry(gui, width=29, textvariable=var3).grid(row=2, column=1)

Label(gui, width=15, text="Postcode: ", bg=geel, fg=blauw).grid(row=3, column=0)
zip_entry= Entry(gui, width=29, textvariable=var4).grid(row=3, column=1)

Label(gui, width=15, text="Huisnummer: ", bg=geel, fg=blauw).grid(row=4, column=0)
housenumber_entry = Entry(gui, width=29, textvariable=var5).grid(row=4, column=1)

Label(gui, width=15, text="Email: ", bg=geel, fg=blauw).grid(row=5, column=0)
email_entry = Entry(gui, width=29, textvariable=var6).grid(row=5, column=1)



# Label(gui, text="Password: ").grid(row=1, sticky=W)
# e2 = Entry(gui, textvariable=var2).grid(row=1, column=1)

def enter():
    #global first_name_entry, insertion_entry, last_name_entry, zip_entry, housenumber_entry, email_entry
    print(first_name_entry)

    first_name = var1.get()
    insertion = var2.get()
    last_name = var3.get()
    zip = var4.get()
    housenumber = var5.get()
    email = var6.get()

    print(username)
    # print(password)

    cursor = db.cursor()
    cursor.execute("INSERT INTO user(unique_code, first_name, insertion, last_name, zip, streetnumber, email, date_time) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", ('ABC', first_name, insertion, last_name, zip, housenumber, email, '2018-10-16 12:00:00'))
    db.commit()

    print(cursor.rowcount)

def printIt():
    print('Kan ff niet nu')

Button(gui, width=15, text="Inloggen" , highlightbackground=blauw, bg=blauw, command=printIt).grid(row=6, column=0)
Button(gui, width=15, text="Registreren" ,highlightbackground=blauw, bg=blauw, command=enter).grid(row=6, column=1)


gui.mainloop()