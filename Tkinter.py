from tkinter import *

#kopieeren van data binnen de GUI
def copy():
    temp = inputbox.get()
    output.insert(END, temp)
    inputbox.delete(0, END)

def NextScreen():
    pass

main = Tk()
main.title("Fietsenstalling")
main.geometry("400x400")

#Frame in het main scherm
GUIFrame = Frame(main)
GUIFrame.grid(row=1, column=0, sticky=S)

#Inputveld
inputbox = Entry(GUIFrame, width = 20, bg = "light grey")
inputbox.grid(row=1, column=0, sticky=W)

#Normale tekst
Label(main, text = "Houd hier uw pas", bg = "red", foreground= "white" ).grid(row=0, column=0, sticky=S)

#kopieert de tekst
Button(GUIFrame, text= "Kopieer de tekst", width=12, command=copy).grid(row=2, column=0, sticky=S)
Button(GUIFrame, text= "naar het volgende scherm", width=24,command=NextScreen).grid(row=6,column=0, sticky=S)
#output veld voor gekopieerde tekst
output = Text(GUIFrame, width=20, height=5, bg="light grey")
output.grid(row=4, column=0, sticky=S)



main.mainloop()


