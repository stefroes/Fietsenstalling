from tkinter import *

def toonLoginFrame():
    toonMainMenu.pack_forget()
    hoofdframe.pack_forget()
    loginframe.pack()

def toonHoofdFrame():
    loginframe.pack_forget()
    hoofdframe.pack()


def toonMainMenu():
    hoofdframe.pack_forget()
    toonMainMenu.pack()
    #label3 = Label(master=toonMainMenu, text='scherm3', background='yellow')
    #label3.pack()



root = Tk()

loginframe = Frame(master=root)
loginframe.pack( expand=True)
#loginfield = Entry(master=loginframe)
#loginfield.pack(padx=10, pady=10)
loginbutton = Button(master=loginframe, text='Houd hier uw pas', command=toonHoofdFrame)
loginbutton.pack(padx=20, pady=20)



hoofdframe = Frame(master=root)
hoofdframe.pack( expand=True)
backbutton = Button(master=hoofdframe, text='volgend scherm', command=toonMainMenu)
backbutton.pack(padx=20, pady=20)

label = Label(master=loginframe, text='scherm1', background='yellow')
label.pack()
label = Label(master=hoofdframe, text='scherm2', background='yellow')
label.pack()


toonMainMenu = Frame(master=root)
hoofdframe.pack( expand=True)
backbutton2 = Button(master=toonMainMenu, text='terug naar scherm 1', command=toonLoginFrame)
backbutton2.pack(padx=20, pady=20)
label3 = Label(master=toonMainMenu, text='scherm3', background='yellow')
label3.pack()

toonLoginFrame()
root.mainloop()
