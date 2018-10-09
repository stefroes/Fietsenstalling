# IMPORT
import datetime
import re


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


email = valid_email()
password = verify_password(valid_password())
date = get_date()

first_name = input('Voornaam: ').capitalize()
last_name = input('Achternaam: ').capitalize()
zip_code = input('Postcode: ').upper().replace(' ', '')
house_number = input('Huisnummer: ').capitalize()


registratie = [first_name, last_name, zip_code, house_number, email, password, date]
