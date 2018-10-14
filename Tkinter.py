from tkinter import *

def copy():
    temp = inputbox.get()
    output.insert(END, temp)
    inputbox.delete(0, END)

main = Tk()
main.title("Fietsenstalling")
main.geometry("400x400")


GUIFrame = Frame(main)
GUIFrame.grid(row=1, column=0, sticky=W)

inputbox = Entry(GUIFrame, width = 20, bg = "light grey")
inputbox.grid(row=1, column=0, sticky=W)

Label(main, text = "Houd hier uw pas").grid(row=0, column=0, sticky=W)
Button(GUIFrame, text= "Kopieer de tekst", width=12, command=copy).grid(row=2, column=0, sticky=W)

output = Text(GUIFrame, width=20, height=5, bg="light grey")
output.grid(row=4, column=0, sticky=W)

main.mainloop()


