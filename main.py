# IMPORT
from MFRC522 import MFRC522
import RPi.GPIO as GPIO
import datetime
import re
import db_connect
import signal
import time
import random
import string

db = db_connect.db

GPIO.setwarnings(False)
GPIO.cleanup()

total_spots = 100
scanning = True


# FUNCTIONS
def valid_email():
    """Check if is valid e-mail"""
    # cursor = db.cursor()

    while True:
        string = input('E-mail: ').lower()

        # DIT KUT DING WERKT NIET GOED, GEEN FK IDEE WAAROM:
        # cursor.execute('SELECT count(userID) FROM `user` WHERE email = %s', string)

        if re.search('[@]', string) is None and len(string) > 5 and re.search('[.]', string) is None:
            print('Voer een geldig email adres in.')
        # elif cursor.fetchone()[0] > 0:
        #    print('Dit e-mail adres is al geregistreerd. Gebruik een andere pas of gebruik een ander e-mail adres.')
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
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_code():
    """Generate a random code with 5 letters and numbers"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


def register(ov):
    """Register a new user"""
    while True:
        email = valid_email()
        date = get_date()
        code = get_code()

        first_name = input('Voornaam: ').capitalize()
        last_name = input('Achternaam: ').capitalize()
        zip_code = input('Postcode: ').upper().replace(' ', '')
        house_number = input('Huisnummer: ').capitalize()

        cursor = db.cursor()
        cursor.execute('INSERT INTO user (unique_code, first_name, last_name, zip, streetnumber, email, ov, date_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (code, first_name, last_name, zip_code, house_number, email, ov, date))
        db.commit()
        cursor.close()

        # STUUR MAIL MET CODE NAAR EMAIL

        scan_ov(ov)


def get_free_spot():
    """Get the first free spot"""
    global total_spots

    cursor = db.cursor()
    cursor.execute('SELECT spot FROM interaction')
    spots = cursor.fetchall()
    cursor.close()

    for free in range(1, total_spots + 1):
        if free not in spots:
            return free

    print('Alle plekken zijn bezet. Wacht totdat er iemand een plek vrijmaakt.')
    return False


def end_read(signal, frame):
    """Capture SIGINT for cleanup when the script is aborted"""
    global reading
    reading = False
    GPIO.cleanup()


def scan_ov(static_ov=False):
    """Check-in and check-out based on chipcard"""
    global scanning

    print('SCANNING: ')

    while scanning:

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
                static_ov = False
            else:
                ov = '{}:{}:{}:{}'.format(uid[0], uid[1], uid[2], uid[3])

            print(ov)

            cursor = db.cursor()
            cursor.execute('SELECT userID FROM user WHERE ov = %s', (ov,))
            user_id = cursor.fetchall()

            found = cursor.rowcount
            cursor.close()

            # USER EXSIST
            if found > 0:
                user_id = user_id[0][0]
                cursor = db.cursor()
                cursor.execute('SELECT spot FROM interaction WHERE userID = %s', (user_id,))

                # INCHECKEN > UITCHECKEN
                if cursor.rowcount > 0:

                    # CHECK IF VALID CODE
                    check = db.cursor()
                    while True:
                        code = input('Vul uw code in: ').capitalize()

                        check.execute('SELECT userID FROM user WHERE unique_code = %s AND userID = %s', (code, user_id))

                        if check.rowcount > 0:
                            print('CODE CORRECT')
                            break
                        else:
                            print('FOUTE CODE, PROBEER OPNIEUW')

                    spot = cursor.fetchall()[0][0]

                    cursor = db.cursor()
                    cursor.execute('DELETE FROM interaction WHERE userID = %s', (user_id,))
                    db.commit()

                    if cursor.rowcount:
                        print('U bent UITGECHECKT op spot #' + str(spot))
                    else:
                        print('Er ging iets mis met uitchecken')

                    cursor.close()

                else:
                    # UITCHECKEN > INCHECKEN
                    cursor = db.cursor()
                    spot = get_free_spot()
                    cursor.execute('INSERT INTO interaction (userID, date, spot) VALUES (%s, %s, %s)', (user_id, get_date(), spot))
                    db.commit()

                    if cursor.rowcount:
                        print('U bent INGECHECKT op spot #' + str(spot))
                    else:
                        print('Er ging iets mis met inchecken')

                    cursor.close()

                cursor.close()

                time.sleep(1)

                print('SCANNING: ')

            else:
                register(ov)


# OV SCAN
scan_ov()
