from tkinter import *
import db_connect
from general.general import *

# GLOBALS
db = db_connect.db
white = '#FFFFFF'
blue = '#013174'
yellow = '#F4C03D'
high_dpi = True
fullscreen = False


class MainScreen:
    def __init__(self, master):
        self.master = master
        self.photo_label = Label(self.master, image=PhotoImage(file='assets/img/main.png'))


class RegisterScreen:
    def __init__(self, master):
        self.master = master

        self.first_name_label = Label(self.master, width=15, text='Voornaam: ', bg=yellow, fg=blue, padx=10, pady=10).grid(row=0, column=0)
        self.first_name_entry = Entry(self.master, width=30)
        self.first_name_entry.grid(row=0, column=1)

        self.insertion_label = Label(self.master, width=15, text='Tussenvoegsels: ', bg=yellow, fg=blue, padx=10, pady=10).grid(row=1, column=0)
        self.insertion_entry = Entry(self.master, width=30)
        self.insertion_entry.grid(row=1, column=1)

        self.last_name_label = Label(self.master, width=15, text='Achternaam: ', bg=yellow, fg=blue, padx=10, pady=10).grid(row=2, column=0)
        self.last_name_entry = Entry(self.master, width=30)
        self.last_name_entry.grid(row=2, column=1)

        self.zip_label = Label(self.master, width=15, text='Postcode: ', bg=yellow, fg=blue, padx=10, pady=10).grid(row=3, column=0)
        self.zip_entry = Entry(self.master, width=30)
        self.zip_entry.grid(row=3, column=1)

        self.streetnumber_label = Label(self.master, width=15, text='Huisnummer: ', bg=yellow, fg=blue, padx=10, pady=10).grid(row=4, column=0)
        self.streetnumber_entry = Entry(self.master, width=30)
        self.streetnumber_entry.grid(row=4, column=1)

        self.email_label = Label(self.master, width=15, text='E-mail: ', bg=yellow, fg=blue, padx=10, pady=10).grid(row=5, column=0)
        self.email_entry = Entry(self.master, width=30)
        self.email_entry.grid(row=5, column=1)

        self.register_button = Button(self.master, width=15, text='Registreren', highlightbackground=blue, bg=blue, fg=white, command=self.register).grid(row=6, column=0)
        self.close_button = Button(self.master, text='New Window', width=15, command=self.new_window).grid(row=6, column=1)

    def register(self):
        data = ('ABCDE', self.first_name_entry.get(), self.insertion_entry.get(), self.last_name_entry.get(), self.zip_entry.get(), self.streetnumber_entry.get(), self.email_entry.get(), '2018-10-16 12:00:00')

        if self.is_valid(self.zip_entry.get(), self.streetnumber_entry.get()):
            cursor = db.cursor()
            cursor.execute('INSERT INTO user(unique_code, first_name, insertion, last_name, zip, streetnumber, email, date_time) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', data)
            db.commit()
            print(cursor.rowcount)

    def is_valid(self, zip_code, streetnumber):
        if len(zip_code) > 7:
            messagebox.showerror('Error', 'Vul een geldig postcode in.')
            return False
        elif len(streetnumber) > 10:
            messagebox.showerror('Error', 'Vul een geldig huisnummer in.')
            return False
        else:
            return True

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Demo2(self.newWindow)


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main():
    root = Tk()

    if high_dpi:
        root.call('tk', 'scaling', 4)
    if fullscreen:
        root.attributes('-fullscreen', True)
    root.geometry('900x700')
    root.configure(bg=yellow)
    root.title('NS Fietsenstalling')

    main = MainScreen(root)
    register = RegisterScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()
