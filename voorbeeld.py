from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

lbl = Label(window, text="Heeft u als een NS-Account?")

lbl.grid(column=0, row=0)


def clicked():
    lbl.configure(text="Login pik")


btn_JA = Button(window, text="Ja", command=clicked)

btn_JA.grid(column=1, row=1)

btn_NEE = Button(window, text="Nee", command=clicked)

btn_NEE.grid(column=3, row=1)

window.mainloop()