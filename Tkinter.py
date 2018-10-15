from tkinter import *

#functie om naar scherm 1 te gaan
def toonLoginFrame():
  toonMainMenu.pack_forget()
  hoofdframe.pack_forget()
  loginframe.pack()

#sfunctie om naar hoofdframe te gaan
def toonHoofdFrame():
  loginframe.pack_forget()
  hoofdframe.pack()

#functie om naar main menu te gaan
def toonMainMenu():
  hoofdframe.pack_forget()
  toonMainMenu.pack()


root = Tk()

#scherm 1

loginframe = Frame(master=root)
loginframe.pack( expand=True)
loginbutton = Button(master=loginframe, text='Houd hier uw pas', command=toonHoofdFrame)
loginbutton.pack(padx=20, pady=20)

#scherm 2

hoofdframe = Frame(master=root)
hoofdframe.pack( expand=True)
backbutton = Button(master=hoofdframe, text='volgend scherm', command=toonMainMenu)
backbutton.pack(padx=20, pady=20)

#scherm 3

toonMainMenu = Frame(master=root)
hoofdframe.pack( expand=True)
backbutton2 = Button(master=toonMainMenu, text='terug naar scherm 1', command=toonLoginFrame)
backbutton2.pack(padx=20, pady=20)


#label scherm 1
label = Label(master=loginframe, text='scherm1', background='yellow')
label.pack()
#label scherm 2
label2 = Label(master=hoofdframe, text='scherm2', background='yellow')
label2.pack()
#label scherm 3
label3 = Label(master=toonMainMenu, text='scherm3', background='yellow')
label3.pack()

toonLoginFrame()
root.mainloop() (edited)
