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

hoofdframe = Frame(master=root, bg='#F4C03D')
hoofdframe.pack(side=TOP, fill="both", expand=True)

loginbutton = Button(master=hoofdframe, bg='#F4C03D', fg='#013174', font='Helvetica 14 bold',
                     text='Algemene informatie', command=toonScherm)
loginbutton.pack(padx=20, pady=20)

infoframe = Frame(master=root, bg='#F4C03D')
infoframe.pack(fill="both", expand=True)

columnNames = ["ID", "Fiets Code", "Voornaam", "Tussenvoegsel", "Achternaam", "Postcode", "Huisnummer", "Email",
               "OV-nummer", "Datum van aanmaken"]

labelPersoonlijk = Label(master=hoofdframe, width=50, bg='#F4C03D', fg='#013174', font='Helvetica 18 bold',
                         text='Dit is wat persoonlijke informatie:')
labelPersoonlijk.pack()
for item in data:
    numberColumn = 2
    for entry in item:
        while numberColumn < 8:
            if data[0][numberColumn] == None:
                numberColumn += 1
            else:
                # labelHeader = Label(master=hoofdframe, width=100, font='Helvetica 10 bold',
                #                     text="{}:\t {}".format(columnNames[numberColumn], data[0][numberColumn]))

                labelHeader = Label(master=hoofdframe, bg='#F4C03D', fg='#013174', font='Helvetica 14 bold',
                                    text="{}:".format(columnNames[numberColumn]))

                labelHeader1 = Label(master=hoofdframe, bg='#F4C03D', fg='#013174', font='Helvetica 12',
                                     text="{}".format(data[0][numberColumn]))

                labelHeader.pack()
                labelHeader1.pack()
                numberColumn += 1

    labelCheckDate = Label(master=hoofdframe, bg='#F4C03D', fg='#013174', font='Helvetica 14 bold',
                           text="Incheck datum:")
    labelCheckDate1 = Label(master=hoofdframe, bg='#F4C03D', fg='#013174', font='Helvetica 12',
                            text=values[0][2])
    labelSpot = Label(master=hoofdframe, bg='#F4C03D', fg='#013174', font='Helvetica 14 bold',
                      text="Parkeerplaats:")
    labelSpot1 = Label(master=hoofdframe, bg='#F4C03D', fg='#013174', font='Helvetica 12',
                       text=values[0][3])
    labelCheckDate.pack()
    labelCheckDate1.pack()
    labelSpot.pack()
    labelSpot1.pack()

    labelFill = Label(master=hoofdframe, bg='#F4C03D', fg='#013174', text='\n')
    labelFill.pack()

backbutton = Button(master=infoframe, bg='#F4C03D', fg='#013174', font='Helvetica 14 bold',
                    text='Persoonlijke informatie', command=toonHoofdFrame)
backbutton.pack(padx=20, pady=20)

labelAlgemeen = Label(master=infoframe, width=50, bg='#F4C03D', fg='#013174', font='Helvetica 18 bold',
                      text='Dit is wat algemene informatie:')
labelAlgemeen.pack()

label = Label(master=infoframe, bg='#F4C03D', fg='#013174', font='Helvetica 12 bold', text=''
                                                                                           'Je moet je fiets parkeren\n'
                                                                                           'Je moet inchecken en uitchecken\n'
                                                                                           'hallo\n'
                                                                                           '')
label.pack()

toonHoofdFrame()
root.mainloop()
