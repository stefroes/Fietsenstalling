from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox
from tkinter.font import Font
import connect
import functions
from classes.user import User
import re
import time
import _thread

# CHECK IF IS RASPBERRY OR PC
simulation = False
try:
    from lib.MFRC522 import MFRC522
    import RPi.GPIO as GPIO
    import signal

    ov_read = True

    GPIO.setwarnings(False)
    GPIO.cleanup()
except ImportError:
    simulation = True
    simulation_ov = '48:127:217:164'

# GLOBALS
db = connect.db
white = '#FFFFFF'
blue = '#013174'
yellow = '#F4C03D'
high_dpi = functions.is_high_resolution()
fullscreen = True


class MainScreen:
    """Main screen class"""
    def __init__(self, master, user=None):
        self.master = master
        self.frame = Frame(self.master, bg=yellow)
        self.frame.pack(fill='both', expand=True)

        self.title = Label(self.frame, width=200, text='Houd uw pas voor de OV reader', bg=yellow, fg=blue)
        self.title.config(font=('Open Sans', 30))
        self.title.pack(pady=(100, 50))

        if high_dpi:
            file = 'ov'
        else:
            file = 'ov_small'

        self.image = PhotoImage(file='images/' + file + '.png')
        self.label = Label(self.frame, image=self.image, bg=yellow)
        self.label.pack(pady=50)

        if user is not None:
            if user.is_registered():
                self.scan(user.get_ov())

        if simulation:
            self.scan_simulation = Entry(self.frame, width=15, justify=CENTER)
            self.scan_simulation.insert(END, simulation_ov)
            self.scan_simulation.pack(pady=25)
            self.scan_submit = Button(self.frame, width=15, text='SCAN', highlightbackground=blue, bg=blue, fg=white, command=self.simulate_scan).pack()
        else:
            self.scan_label = Label(self.frame, width=100, text='Scanning...', bg=yellow, fg=blue, padx=10, pady=10).pack()

            self.master.after(0, self.scan)

    @staticmethod
    def end_read():
        """"Cleanup GPIO pins for RFID-RC522 chip"""
        global ov_read
        ov_read = False
        GPIO.cleanup()

    def scan(self, static_ov=None):
        """Scan OV card with RFID-RC522 chip"""
        global ov_read

        if static_ov:
            ov = static_ov
            user = User(ov)
            ov_read = False

            if user.is_registered():
                self.frame.pack_forget()
                InfoScreen(self.master, user)
            else:
                self.frame.pack_forget()
                RegisterScreen(self.master, user.get_ov())
        else:
            reader = MFRC522()

            # Hook the SIGINT, Scan for cards
            signal.signal(signal.SIGINT, self.end_read)

            reader.MFRC522_Request(reader.PICC_REQIDL)

            # Get the UID of the card
            (status, uid) = reader.MFRC522_Anticoll()

            # If we have the UID, continue
            if status == reader.MI_OK:
                ov = '{}:{}:{}:{}'.format(uid[0], uid[1], uid[2], uid[3])
                user = User(ov)
                ov_read = False

                if user.is_registered():
                    self.frame.pack_forget()
                    InfoScreen(self.master, user)
                else:
                    self.frame.pack_forget()
                    RegisterScreen(self.master, user.get_ov())
            else:
                self.master.after(200, self.scan)

    def simulate_scan(self):
        """Simulate OV card scan by entering the serial key"""
        user = User(self.scan_simulation.get())

        if user.is_registered():
            self.frame.pack_forget()
            InfoScreen(self.master, user)
        else:
            self.frame.pack_forget()
            RegisterScreen(self.master, user.get_ov())


class InfoScreen:
    """Info screen class"""
    def __init__(self, master, user):
        self.master = master
        self.user = user

        self.frame = None
        self.title = None
        self.code_entry_label = None
        self.code_entry = None
        self.code_button = None
        self.progress = None
        self.close_button = None
        self.detail = None
        self.detail_frame = None
        self.timer = 5

        if self.user.is_registered():
            if self.user.is_checked_in():
                self.check_out()
            else:
                self.check_in()

    def check_in(self):
        """View screen for checked in user"""
        self.frame = Frame(self.master, bg=yellow)
        self.frame.pack(anchor=CENTER)

        spot = self.user.check_in()
        if spot:
            self.title = Label(self.frame, width=200, text='Ingecheckt op spot:\n#' + str(spot), bg=yellow, fg=blue)
            self.title.config(font=('Open Sans', 30))
            self.title.pack(pady=(25, 50))

            _thread.start_new_thread(self.disappear, ())
        else:
            messagebox.showerror('Inchecken mislukt', 'Alle plekken zijn bezet. Wacht totdat er iemand een plek vrijmaakt.')

    def check_out(self):
        """View screen for checked out user"""
        self.frame = Frame(self.master, bg=yellow)
        self.frame.pack(anchor=CENTER)

        self.title = Label(self.frame, width=200, text='Uitchecken', bg=yellow, fg=blue)
        self.title.config(font=('Open Sans', 30))
        self.title.pack(pady=(100, 50))

        self.code_entry_label = Label(self.frame, width=15, text='Vul uw code in:', bg=yellow, fg=blue, padx=10, pady=10)
        self.code_entry_label.pack(pady=25)
        self.code_entry = Entry(self.frame, width=30)
        self.code_entry.pack(pady=25)

        self.code_button = Button(self.frame, width=15, text='Uitchecken', highlightbackground=blue, bg=blue, fg=white, command=self.check_out_command)
        self.code_button.pack()

    def check_out_command(self):
        """Validates user code and continues if success """
        spot = self.user.check_out(self.code_entry.get())
        if spot:
            self.title.pack_forget()
            self.code_entry_label.pack_forget()
            self.code_entry.pack_forget()
            self.code_button.pack_forget()

            self.title = Label(self.frame, width=200, text='Uitgecheckt op spot:\n#' + str(spot), bg=yellow, fg=blue)
            self.title.config(font=('Open Sans', 30))
            self.title.pack(pady=(25, 50))

            _thread.start_new_thread(self.disappear, ())
        else:
            messagebox.showerror('Uitchecken mislukt', 'Sorry ' + self.user.get_first_name() + ', probeer opnieuw uit te checken.')

    def disappear(self, wait=True):
        """Destroy the user views"""
        global ov_read

        if wait:
            self.progress = Label(self.frame, width=200, text='Dit scherm sluit in ' + str(self.timer), bg=yellow, fg=blue)
            self.progress.pack()

            self.detail_frame = Frame(self.master, bg=yellow)
            self.detail_frame.pack(anchor=CENTER)

            self.close_button = Button(self.frame, text='Bekijk uw profiel', width=30, command=self.show_details)
            self.close_button.pack(pady=(25, 50))

            while self.timer >= 0:
                self.progress.configure(text='Dit scherm sluit in ' + str(self.timer))
                time.sleep(1)
                self.timer -= 1

        self.frame.destroy()
        self.detail_frame.destroy()

        ov_read = True
        MainScreen(self.master)

    def show_details(self):
        """Show user information when clicked"""
        self.close_button.pack_forget()
        self.timer = 11

        DetailScreen(self.master, self.detail_frame, self.user)


class RegisterScreen:
    """Register screen class"""
    def __init__(self, master, ov):
        self.master = master

        self.frame = Frame(self.master, bg=yellow)
        self.frame.pack(fill=None, expand=False)

        self.ov = ov

        self.title = Label(self.frame, width=150, text='Registeren', bg=yellow, fg=blue)
        self.title.config(font=('Open Sans', 30))
        self.title.pack(pady=(25, 25))

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

        self.close_button = Button(self.frame, text='Annuleren', width=15, command=self.cancel).pack(pady=(10, 10))
        self.register_button = Button(self.frame, width=15, text='Registreren', highlightbackground=blue, bg=blue, fg=white, command=self.register).pack()

    def register(self):
        """Get, validate and convert user input data"""
        first_name = self.first_name_entry.get()
        insertion = self.insertion_entry.get()
        last_name = self.last_name_entry.get()
        zip_code = self.zip_entry.get()
        streetnumber = self.streetnumber_entry.get()
        email = self.email_entry.get()

        # Validate input
        if self.is_valid(first_name, last_name, zip_code, streetnumber, email):
            d = self.convert(first_name, insertion, last_name, zip_code, streetnumber, email)

            check = User(self.ov).register(d['first_name'], d['insertion'], d['last_name'], d['zip_code'], d['streetnumber'], d['email'])

            if check:
                user = User(self.ov)

                self.frame.pack_forget()
                MainScreen(self.master, user)

                return True
            else:
                return False

    @staticmethod
    def is_valid(first_name, last_name, zip_code, streetnumber, email):
        """Check if user input is valid"""
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
        """Convert user input to clean strings"""
        return {
            'first_name': functions.clean(first_name),
            'insertion': functions.clean(insertion, False, False, True),
            'last_name': functions.clean(last_name),
            'zip_code': functions.clean(zip_code, False, uppercase=True),
            'streetnumber': functions.clean(streetnumber, False, uppercase=True),
            'email': functions.clean(email, False, lowercase=True)
        }

    def cancel(self):
        """Cancel register process and return to the main screen"""
        self.frame.pack_forget()
        MainScreen(self.master)


class DetailScreen:
    """Detail screen class"""
    def __init__(self, master, frame, user):
        self.master = master
        self.user = user

        self.frame = frame

        if self.user.is_registered():
            self.title = Label(self.frame, width=150, text='Info', bg=yellow, fg=blue)
            self.title.config(font=('Open Sans', 30))
            self.title.pack(pady=(25, 50))

            self.full_name_label = Label(self.frame, width=200, text='Naam: ' + self.user.get_full_name(), bg=yellow, fg=blue, padx=10, pady=10).pack()

            self.zip_label = Label(self.frame, width=200, text='Postcode: ' + self.user.get_zip(), bg=yellow, fg=blue, padx=10, pady=10).pack()

            self.streetnumber_label = Label(self.frame, width=200, text='Huisnummer: ' + self.user.get_streetnumber(), bg=yellow, fg=blue, padx=10, pady=10).pack()

            self.email_label = Label(self.frame, width=200, text='E-mail: ' + self.user.get_email(), bg=yellow, fg=blue, padx=10, pady=10).pack()

            self.registered_label = Label(self.frame, width=200, text='Geregistreerd op: ' + self.user.get_registered(), bg=yellow, fg=blue, padx=10, pady=10).pack()


def main():
    """Init and start the program"""
    root = Tk()
    if high_dpi:
        root.call('tk', 'scaling', 4)
    if fullscreen:
        root.attributes('-fullscreen', True)
    root.configure(bg=yellow)
    root.grid_columnconfigure(2, weight=1)
    root.title('NS Fietsenstalling')

    MainScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()
