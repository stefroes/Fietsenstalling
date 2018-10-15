import tkinter

def speak():
    print('Hi')

main=Tk()
main.title("NS-fietsenstalling")
main.geometry("400x400")

Label(main, text="Welkom bij de NS-fietsenstalling").grid(row=0, column=0, sticky=W)

Button(main, text="My button", width=12, command=speak).grid(row=1, column=0, sticky=W)

main.mainloop()