import mysql.connector
import datetime
import random
import string
import time
import connect
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# GLOBALS
db = connect.db


class User:

    def __init__(self, ov):
        self.ov = ov

        cursor = db.cursor()
        cursor.execute('SELECT userID, first_name, insertion, last_name, zip, streetnumber, email, code, registered FROM user WHERE ov = %s', (ov,))
        data = cursor.fetchone()

        if cursor.rowcount == 1:
            self.user_id = data[0]
            self.first_name = data[1]
            self.insertion = data[2]
            self.last_name = data[3]
            self.zip = data[4]
            self.streetnumber = data[5]
            self.email = data[6]
            self.code = data[7]
            self.registered = data[8]
            self.valid = True
        else:
            self.valid = False

    def get_user_id(self):
        """Get user ID"""
        return self.user_id

    def get_code(self):
        """Get user code"""
        return self.code

    def get_first_name(self):
        """Get user firstname"""
        return self.first_name

    def get_last_name(self):
        """Get user lastname"""
        return self.last_name

    def get_full_name(self):
        """Get user full name"""
        if self.insertion:
            return self.first_name + ' ' + self.insertion + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name

    def get_zip(self):
        """Get zip code of user"""
        return self.zip[:4] + ' ' + self.zip[4:6]

    def get_streetnumber(self):
        """Get streetnumber of user"""
        return self.streetnumber

    def get_email(self):
        """Get user email"""
        return self.email

    def get_ov(self):
        """Get user OV serial key"""
        return self.ov

    def get_registered(self):
        """Get user registered date"""
        return self.registered.strftime('%d %B %Y')

    def is_registered(self):
        """Check if is valid user"""
        return self.valid

    @staticmethod
    def get_free_spot():
        """Get the first free spot if available"""
        total_spots = 100

        cursor = db.cursor()
        cursor.execute('SELECT spot FROM interaction')
        spots = cursor.fetchall()
        cursor.close()

        for free in range(1, total_spots + 1):
            if free not in spots:
                return free

        return False

    @staticmethod
    def get_current_date():
        """Get current datetime"""
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def generate_code():
        """Generate a random code with 5 letters and numbers"""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    def check_in(self):
        """Check the user in to the database"""
        cursor = db.cursor()
        spot = self.get_free_spot()
        cursor.execute('INSERT INTO interaction (userID, date, spot) VALUES (%s, %s, %s)', (self.get_user_id(), self.get_current_date(), spot))
        db.commit()

        if cursor.rowcount:
            return spot
        else:
            return False

    def check_out(self, code):
        """Check the user out to the databyase"""
        cursor = db.cursor()
        cursor.execute('SELECT spot FROM interaction WHERE userID = %s', (self.get_user_id(),))

        if cursor.rowcount > 0:
            check = db.cursor()
            while True:
                check.execute('SELECT userID FROM user WHERE code = %s AND userID = %s', (code, self.get_user_id()))

                if check.rowcount > 0:
                    break
                else:
                    return False

            spot = cursor.fetchone()[0]

            cursor = db.cursor()
            cursor.execute('DELETE FROM interaction WHERE userID = %s', (self.get_user_id(),))
            db.commit()

            if cursor.rowcount:
                return spot
            else:
                return False

    def is_checked_in(self):
        """Check is user is checked in"""
        cursor = db.cursor()
        cursor.execute('SELECT spot FROM interaction WHERE userID = %s', (self.get_user_id(),))
        return cursor.rowcount > 0

    def scan(self, code=False):
        """Trigger user OV scan"""
        if self.is_checked_in():
            self.check_out(code)
        else:
            self.check_in()

    def register(self, first_name, insertion, last_name, zip_code, streetnumber, email):
        """Register a new user"""
        code = self.generate_code()

        cursor = db.cursor()
        cursor.execute('INSERT INTO user(first_name, insertion, last_name, zip, streetnumber, email, ov, code, registered) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (first_name, insertion, last_name, zip_code, streetnumber, email, self.ov, code, self.get_current_date()))
        db.commit()

        self.first_name = first_name
        self.insertion = insertion
        self.last_name = last_name
        self.send_mail(self.get_full_name(), email, code)

        return cursor.rowcount == 1

    @staticmethod
    def send_mail(name, to, code):
        """Send mail with code to registered user"""
        msg = MIMEMultipart()

        message = 'Beste {},<br><br>' \
                  'Bedankt voor het gebruiken van onze fietsenstalling.<br>' \
                  'Hier is uw fiets code: <br>' \
                  '<h1>{}</h1>' \
                  'Deze code heeft u nodig om uw fiets uit te checken, bewaar deze code daarom goed! <br>' \
                  '<br>' \
                  'Met vriendelijke groeten, <br><br>' \
                  'NS Fietsenstalling'.format(name, code)

        password = 'identificatiesysteem'
        msg['From'] = 'fietsenstallingv1a@gmail.com'
        msg['To'] = to
        msg['Subject'] = 'NS Fietsenstalling Code {}'.format(code)

        msg.attach(MIMEText(message, 'HTML'))

        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()
