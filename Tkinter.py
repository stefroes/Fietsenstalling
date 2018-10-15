from tkinter import *

def toonLoginFrame():
    hoofdframe.pack_forget()
    loginframe.pack()


def toonHoofdFrame():
    loginframe.pack_forget()
    hoofdframe.pack()


def login():
    if loginfield.get() == "ja":
        toonHoofdFrame()
    else:
        print('Verkeerde gebruikersnaam!')


root = Tk()

label = Label(master=root, text='Welkom bij de NS fietsenstallning.', height=2)
label.pack()

loginframe = Frame(master=root)
loginframe.pack(fill="both", expand=True)
loginfield = Entry(master=loginframe)
loginfield.pack(padx=20, pady=20)
loginbutton = Button(master=loginframe, text='login', command=login)
loginbutton.pack(padx=20, pady=20)

hoofdframe = Frame(master=root)
hoofdframe.pack(fill="both", expand=True)
backbutton = Button(master=hoofdframe, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)

toonLoginFrame()
root.mainloop()
