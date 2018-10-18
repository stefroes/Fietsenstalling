from tkinter import *
import db_connect

blauw = '#003373'
geel = '#ffac00'

gui = Tk()
gui.attributes('-fullscreen', True)
gui.geometry('700x650')
gui.configure(bg=geel)

db = db_connect.db

gui.title("Login NS fietsenstalling")

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()

login = Frame(master=gui)
Label(gui, width=15, text="Voornaam: ", bg=geel).grid(row=0, column=0)
first_name_entry = Entry(gui, width=29, textvariable=var1).grid(row=0, column=1)

Label(gui, width=15, text="Tussenvoegsels: ", bg=geel).grid(row=1, column=0)
insertion_entry = Entry(gui, width=29, textvariable=var2).grid(row=1, column=1)

Label(gui, width=15, text="Achternaam: ", bg=geel).grid(row=2, column=0)
last_name_entry = Entry(gui, width=29, textvariable=var3).grid(row=2, column=1)

Label(gui, width=15, text="Postcode: ", bg=geel).grid(row=3, column=0)
zip_entry = Entry(gui, width=29, textvariable=var4).grid(row=3, column=1)

Label(gui, width=15, text="Huisnummer: ", bg=geel).grid(row=4, column=0)
housenumber_entry = Entry(gui, width=29, textvariable=var5).grid(row=4, column=1)

Label(gui, width=15, text="Email: ", bg=geel).grid(row=5, column=0)
email_entry = Entry(gui, width=29, textvariable=var6).grid(row=5, column=1)


def enter():
    print(first_name_entry)

    first_name = var1.get()
    insertion = var2.get()
    last_name = var3.get()
    zip = var4.get()
    housenumber = var5.get()
    email = var6.get()

    cursor = db.cursor()
    cursor.execute("INSERT INTO user(unique_code, first_name, insertion, last_name, zip, streetnumber, email, date_time) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", ('ABC', first_name, insertion, last_name, zip, housenumber, email, '2018-10-16 12:00:00'))
    db.commit()

    print(cursor.rowcount)


Button(gui, width=15, text="Inloggen", highlightbackground=blauw, bg=blauw).grid(row=6, column=0)
Button(gui, width=15, text="Registreren", highlightbackground=blauw, bg=blauw, command=enter).grid(row=6, column=1)

gui.mainloop()


class main_screen:
    def __init__(self, master):
        self.master = master