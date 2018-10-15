# IMPORT
from MFRC522 import MFRC522
import RPi.GPIO as GPIO
import datetime
import re
import db_connect
import signal
import time

db = db_connect.db


# FUNCTIONS
def valid_email():
    """Check if is valid E-mail"""
    while True:
        string = input('E-mail: ').lower()
        if re.search('[@]', string) is None:
            print('Voer een geldig email adres in.')
        elif re.search('[.]', string) is None:
            print('Voer een geldig email adres in.')
        else:
            return string


def valid_password():
    """Check if is valid password"""
    while True:
        string = input('Wachtwoord (Minmaal 8 karakters, 1 hoofdletter en 1 cijfer): ')
        if len(string) < 8:
            print('Wachtwoord moet minimaal 8 karakters bevatten.')
        elif re.search('[0-9]', string) is None:
            print('Wachtwoord moet minimaal 1 cijfer bevatten.')
        elif re.search('[A-Z]', string) is None:
            print('Wachtwoord moet minimaal 1 hoofdletter bevatten.')
        else:
            return string


def verify_password(string):
    """Verify two password to be the same"""
    while True:
        check = input('Herhaal wachtwoord: ')
        if check != string:
            print('Dit moet gelijk zijn aan je wachtwoord.')
        else:
            return string


def get_date():
    """Get current datetime"""
    return datetime.datetime.now().strftime('%d-%m-%G %H:%M:%S')


def register():
    email = valid_email()
    password = verify_password(valid_password())
    date = get_date()

    first_name = input('Voornaam: ').capitalize()
    last_name = input('Achternaam: ').capitalize()
    zip_code = input('Postcode: ').upper().replace(' ', '')
    house_number = input('Huisnummer: ').capitalize()

    print([first_name, last_name, zip_code, house_number, email, password, date])


reading = True


def get_free_spot():
    return 1


# Capture SIGINT for cleanup when the script is aborted
def end_read(signal, frame):
    global reading
    reading = False
    GPIO.cleanup()


# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

MIFAREReader = MFRC522.MFRC522()

print("SCANNING: ")

# OV SCAN
while reading:

    # Scan for cards
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print("Card detected")

    # Get the UID of the card
    (status, uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        ov = '{}:{}:{}:{}'.format(uid[0], uid[1], uid[2], uid[3])
        print(ov)

        cursor = db.cursor()
        cursor.execute('SELECT user.userID, interaction.spot FROM user INNER JOIN interaction ON user.userID = interaction.userID WHERE ov = %s', (ov,))
        data = cursor.fetchall()
        cursor.close()

        if cursor.rowcount > 0:
            userID = data[0]
            spot = data[1]

            # INCHECKEN > UITCHECKEN
            if cursor.rowcount != 0:
                cursor = db.cursor()
                cursor.execute('DELETE FROM interaction WHERE userID = %s', (userID))
                db.commit()
                cursor.close()
                print(cursor.rowcount)

                if cursor.rowcount:
                    print('U bent UITGECHECKT op spot #' + str(spot))
                else:
                    print('Er ging iets mis met uitchecken')

            else:
                # UITCHECKEN > INCHECKEN
                cursor = db.cursor()
                spot = get_free_spot()
                cursor.execute('INSERT INTO interaction (userID, date, spot) VALUES (%s, %s, %s)', (userID, get_date(), spot))
                db.commit()
                cursor.close()

                if cursor.rowcount:
                    print('U bent INGECHECKT op spot #' + str(spot))
                else:
                    print('Er ging iets mis met inchecken')

            time.sleep(1)

        else:
            register()
