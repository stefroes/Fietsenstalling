from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import db_connect
from classes.user import User
import re
import time
import _thread

# CHECK IF IS RASPBERRY OR PC
emulator = False
try:
    from lib import MFRC522
    import RPi.GPIO as GPIO
    import signal

    GPIO.setwarnings(False)
    GPIO.cleanup()
except ImportError:
    emulator = True
    emulator_ov = '48:127:217:164'

# GLOBALS
db = db_connect.db
white = '#FFFFFF'
blue = '#013174'
yellow = '#F4C03D'
high_dpi = True
fullscreen = False


def clean(string, capitalize=True, remove_spaces=True, lowercase=False, uppercase=False):
    if capitalize:
        string = string.capitalize()
    elif lowercase:
        string = string.lower()
    elif uppercase:
        string = string.upper()
    if remove_spaces:
        string = string.replace(' ', '')

    return string


class MainScreen:
    def __init__(self, master, user=None):
        self.master = master
        self.frame = Frame(self.master, bg=yellow)
        self.frame.pack()

        self.title = Label(self.frame, width=200, text='Houd uw pas voor de OV reader', bg=yellow, fg=blue)
        self.title.config(font=('Open Sans', 30))
        self.title.pack(pady=(100, 50))

        self.image = PhotoImage(file='assets/img/ov.png')
        self.label = Label(self.frame, image=self.image, bg=yellow)
        self.label.pack(pady=50)

        if user is not None:
            if user.is_registered():
                self.scan(user.get_ov())

        if emulator:
            self.scan_emulator = Entry(self.frame, width=15, justify=CENTER)
            self.scan_emulator.insert(END, emulator_ov)
            self.scan_emulator.pack(pady=25)
            self.scan_submit = Button(self.frame, width=15, text='SCAN', highlightbackground=blue, bg=blue, fg=white, command=self.emulate_scan).pack()
        else:
            self.scan_label = Label(self.frame, width=100, text='Scanning...', bg=yellow, fg=blue, padx=10, pady=10).pack()
            self.scan()

    @staticmethod
    def scan(static_ov=None):
        print('SCANNING: ')

        while True:
            # Hook the SIGINT, # Scan for cards
            signal.signal(signal.SIGINT, end_read)
            reader = MFRC522.MFRC522()
            (status, TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)

            # If a card is found
            if status == reader.MI_OK:
                print('Card detected')

            # Get the UID of the card
            (status, uid) = reader.MFRC522_Anticoll()

            # If we have the UID, continue
            if status == reader.MI_OK or static_ov:

                if static_ov:
                    ov = static_ov
                    static_ov = None
                else:
                    ov = '{}:{}:{}:{}'.format(uid[0], uid[1], uid[2], uid[3])

                user = User(ov)
                print(user)

                print(user.is_checked_in())

    def emulate_scan(self):
        user = User(self.scan_emulator.get())

        if user.is_registered():
            self.frame.pack_forget()
            InfoScreen(self.master, user)
        else:
            self.frame.pack_forget()
            RegisterScreen(self.master, user.get_ov())


class InfoScreen:
    def __init__(self, master, user):
        self.master = master
        self.user = user

        self.frame = None
        self.title = None
        self.code_entry_label = None
        self.code_entry = None
        self.code_button = None

        if self.user.is_registered():
            if self.user.is_checked_in():
                self.check_out()
            else:
                self.check_in()

    def check_in(self):
        self.frame = Frame(self.master, bg=yellow)
        self.frame.pack()

        spot = self.user.check_in()
        if spot:
            self.title = Label(self.frame, width=200, text='INGECHECKT OP SPOT : ' + str(spot), bg=yellow, fg=blue)
            self.title.config(font=('Open Sans', 30))
            self.title.pack(pady=(100, 50))

            print('INGECHECKT')

            _thread.start_new_thread(self.disappear, ())
        else:
            messagebox.showerror('Inchecken mislukt', 'Incorrecte code')

    def check_out(self):
        self.frame = Frame(self.master, bg=yellow)
        self.frame.pack()

        self.title = Label(self.frame, width=200, text='Uitchecken', bg=yellow, fg=blue)
        self.title.config(font=('Open Sans', 30))
        self.title.pack(pady=(100, 50))

        self.code_entry_label = Label(self.frame, width=15, text='Vul uw code in:', bg=yellow, fg=blue, padx=10, pady=10)
        self.code_entry_label.pack()
        self.code_entry = Entry(self.frame, width=30)
        self.code_entry.pack()

        self.code_button = Button(self.frame, width=15, text='Uitchecken', highlightbackground=blue, bg=blue, fg=white, command=self.check_out_command)
        self.code_button.pack()

    def check_out_command(self):
        spot = self.user.check_out(self.code_entry.get())
        if spot:
            self.title.pack_forget()
            self.code_entry_label.pack_forget()
            self.code_entry.pack_forget()
            self.code_button.pack_forget()

            self.title = Label(self.frame, width=200, text='UITGECHECKT OP SPOT ' + str(spot), bg=yellow, fg=blue)
            self.title.config(font=('Open Sans', 30))
            self.title.pack(pady=(100, 50))

            _thread.start_new_thread(self.disappear, ())
        else:
            messagebox.showerror('Uitchecken mislukt', 'Sorry ' + self.user.get_first_name() + ', probeer opnieuw uit te checken.')

    def disappear(self):
        countdown = 3
        print('REMAIN FOR 3 SECONDS')
        while countdown >= 0:
            print(countdown, end='...')
            time.sleep(1)
            countdown -= 1
        print('END\n')

        self.frame.destroy()
        MainScreen(self.master)


class RegisterScreen:

    def __init__(self, master, ov):
        self.master = master

        self.frame = Frame(self.master, width=900, bg=yellow)
        self.frame.pack(fill=None, expand=False)

        self.ov = ov

        self.title = Label(self.frame, width=150, text='Registeren', bg=yellow, fg=blue)
        self.title.config(font=('Open Sans', 30))
        self.title.pack(pady=(100, 50))

        self.first_name_label = Label(self.frame, width=15, text='Voornaam: ', bg=yellow, fg=blue, padx=10, pady=10).pack()
        self.first_name_entry = Entry(self.frame, width=30)
        self.first_name_entry.pack()

        self.insertion_label = Label(self.frame, width=15, text='Tussenvoegsels: ', bg=yellow, fg=blue, padx=10, pady=10).pack()
        self.insertion_entry = Entry(self.frame, width=30)
        self.insertion_entry.pack()

        self.last_name_label = Label(self.frame, width=15, text='Achternaam: ', bg=yellow, fg=blue, padx=10, pady=10).pack()
        self.last_name_entry = Entry(self.frame, width=30)
        self.last_name_entry.pack()

        self.zip_label = Label(self.frame, width=15, text='Postcode: ', bg=yellow, fg=blue, padx=10, pady=10).pack()
        self.zip_entry = Entry(self.frame, width=30)
        self.zip_entry.pack()

        self.streetnumber_label = Label(self.frame, width=15, text='Huisnummer: ', bg=yellow, fg=blue, padx=10, pady=10).pack()
        self.streetnumber_entry = Entry(self.frame, width=30)
        self.streetnumber_entry.pack()

        self.email_label = Label(self.frame, width=15, text='E-mail: ', bg=yellow, fg=blue, padx=10, pady=10).pack()
        self.email_entry = Entry(self.frame, width=30)
        self.email_entry.pack()

        self.close_button = Button(self.frame, text='Annuleren', width=15, command=self.cancel).pack(padx=(50, 50), side=LEFT)
        self.register_button = Button(self.frame, width=15, text='Registreren', highlightbackground=blue, bg=blue, fg=white, command=self.register).pack(padx=(50, 50), side=LEFT)

    def register(self):
        first_name = self.first_name_entry.get()
        insertion = self.insertion_entry.get()
        last_name = self.last_name_entry.get()
        zip_code = self.zip_entry.get()
        streetnumber = self.streetnumber_entry.get()
        email = self.email_entry.get()

        # VALIDATE INPUT
        if self.is_valid(first_name, last_name, zip_code, streetnumber, email):
            print('VALID')
            d = self.convert(first_name, insertion, last_name, zip_code, streetnumber, email)

            check = User(self.ov).register(d['first_name'], d['insertion'], d['last_name'], d['zip_code'], d['streetnumber'], d['email'])

            if check:
                user = User(self.ov)

                print('REGISTER SUCCESS')

                self.frame.pack_forget()
                MainScreen(self.master, user)

                return True
            else:
                return False

    @staticmethod
    def is_valid(first_name, last_name, zip_code, streetnumber, email):
        if len(first_name) < 1:
            messagebox.showerror('Error', 'Vul een geldige voornaam in.')
            return False
        elif len(last_name) < 1:
            messagebox.showerror('Error', 'Vul een geldige achternaam in.')
            return False
        elif len(zip_code.replace(' ', '')) != 6:
            messagebox.showerror('Error', 'Vul een geldig postcode in.')
            return False
        elif 1 < len(streetnumber) > 10:
            messagebox.showerror('Error', 'Vul een geldig huisnummer in.')
            return False
        elif re.search('[@]', email) is None or len(email) < 5 or re.search('[.]', email) is None:
            messagebox.showerror('Error', 'Vul een geldig e-mail in.')
            return False
        else:
            return True

    @staticmethod
    def convert(first_name, insertion, last_name, zip_code, streetnumber, email):
        return {
            'first_name': clean(first_name),
            'insertion': clean(insertion, False, False, True),
            'last_name': clean(last_name),
            'zip_code': clean(zip_code, False, uppercase=True),
            'streetnumber': clean(streetnumber, False, uppercase=True),
            'email': clean(email, False, lowercase=True)
        }

    def cancel(self):
        self.frame.pack_forget()
        MainScreen(self.master)


def main():
    root = Tk()
    if high_dpi:
        root.call('tk', 'scaling', 4)
    if fullscreen:
        root.attributes('-fullscreen', True)
    root.geometry('900x700')
    root.configure(bg=yellow)
    root.grid_columnconfigure(2, weight=1)
    root.title('NS Fietsenstalling')

    main = MainScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()
