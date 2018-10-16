from tkinter import *
import db_connect


def toonInfoFrame():
    hoofdframe.pack_forget()
    infoframe.pack()


def toonHoofdFrame():
    infoframe.pack_forget()
    hoofdframe.pack()


def toonScherm():
    toonInfoFrame()


# Zorg dat dit bestand met het database bestand kan communniceren door de waarde te pakken uit het database bestand.
db = db_connect.db

ovnummer = '48:127:217:164'

# Query om de correcte gebruiker te selecteren.
userQuery = "SELECT * FROM user WHERE ov = '{}'".format(ovnummer)

# Voer de query uit.
cursor = db.cursor()
cursor.execute(userQuery)

# Zet het resultaat van de query in een waarde.
data = cursor.fetchall()

cursor.close()

interactionQuery = "SELECT * FROM interaction WHERE userID = {}".format(data[0][0])
print(interactionQuery)

# Voer de query uit.
cursor = db.cursor()
cursor.execute(interactionQuery)

# Zet het resultaat van de query in een waarde.
values = cursor.fetchall()

cursor.close()

root = Tk()

hoofdframe = Frame(master=root)
hoofdframe.pack(side=TOP, fill="both", expand=True)

loginbutton = Button(master=hoofdframe, text='login', command=toonScherm)
loginbutton.pack(padx=20, pady=20)

infoframe = Frame(master=root)
infoframe.pack(fill="both", expand=True)

columnNames = ["ID", "Fiets Code", "Voornaam", "Tussenvoegsel", "Achternaam", "Postcode", "Huisnummer", "Email",
               "OV-nummer", "Datum van aanmaken"]

labelPersoonlijk = Label(master=hoofdframe, width=50, font='Helvetica 18 bold',
                         text='Dit is wat persoonlijke informatie:\n')
labelPersoonlijk.pack()
for item in data:
    numberColumn = 0
    for entry in item:
        labelHeader = Label(master=hoofdframe, width=100, font='Helvetica 10 bold',
                            text="{}:\t\t\t {}".format(columnNames[numberColumn], data[0][numberColumn]))

        labelHeader.pack()
        numberColumn += 1

    labelCheckDate = Label(master=hoofdframe, width=100, font='Helvetica 10 bold',
                           text="Incheck datum:\t\t\t {}".format(values[0][2]))
    labelSpot = Label(master=hoofdframe, width=100, font='Helvetica 10 bold',
                      text="Parkeerplaats:\t\t\t {}".format(values[0][3]))
    labelCheckDate.pack()
    labelSpot.pack()

    labelFill = Label(master=hoofdframe, text='\n')
    labelFill.pack()

# cursor.description[numberColumn][0]
labelAlgemeen = Label(master=infoframe, width=50, font='Helvetica 18 bold', text='Dit is wat algemene informatie:\n')
labelAlgemeen.pack()

label = Label(master=infoframe, text=''
                                     'Je moet je fiets parkeren\n'
                                     'Je moet inchecken en uitchecken\n'
                                     'hallo\n'
                                     '')
label.pack()
backbutton = Button(master=infoframe, text='Terug', command=toonHoofdFrame)
backbutton.pack(padx=20, pady=20)

toonHoofdFrame()
root.mainloop()
