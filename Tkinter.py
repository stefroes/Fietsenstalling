from tkinter import *

def speak():
    print("zoek het zelf uit")

main = Tk()
main.title("Fietsenstalling")
main.geometry("400x400")

Label(main, text = "Houd hier uw pas").grid(row=0, column=0, sticky=W)
Button(main, text= "help", width=12, command=speak).grid(row=1, column=0, sticky=W)



main.mainloop()


