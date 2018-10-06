import re
import db_connect

# Zorg dat dit bestand met het database bestand kan communniceren door de waarde te pakken uit het database bestand.
db = db_connect.db

# --- MYSQL INSTALLEREN
# GA NAAR FILE -> SETTINGS -> PROJECT -> PROJECT INTERPRETER -> KLIK RECHTS OP HET PLUS ICON
# ZOEK NAAR 'mysql-connector', KIES DEZE EN KLIK OP 'Install Package'


# --- INLOGGEN OP DATABASE
# https://roeswebdesign.nl:8443/domains/databases/phpMyAdmin/
# username: fietsen_user
# password: QYm6Pt3Cv4cDNynT

print("Welkom bij de NS - fietsenstalling.\n")

new_customer = input('Heeft u al een account bij de NS-fietsenstalling? Type ja of nee: ').lower()

if new_customer == 'nee':
    print(
        '\nOm uw fiets te kunnen stallen in de NS-fietsenstalling dient u eerst een account aan te maken. Volg alstublieft de volgende stappen:\n')
    while True:
        first_name = input('Vul hier uw voornaam in: ').capitalize()
        if bool(re.search(r'\d', first_name)) == True or first_name == '' or first_name == ' ':
            print('Voer een geldige waarde in')
        else:
            break

    insertion = input('Vul hier uw tussenvoegsels in: ')
    last_name = input('Vul hier uw achternaam in: ').capitalize()
    zip = input('Vul hier uw postcode in: ').replace(' ', '').upper()
    number = input('Vul hier uw huisnummer in: ')
    goed_email = ''


    def email(email):
        while True:
            email = str(input('Vul hier uw Email in: '))
            if re.search('[@]', email) is None:
                print("Voer een geldig email adres in.")
            elif re.search('[.]', email) is None:
                print("Voer een geldig email adres in.")
            else:
                return email
                print("Email voldoet aan voorwaarden")
                break


    goed_email = email(email)
    goed_wachtwoord = ''


    def wachtwoord(wachtwoord):
        while True:
            wachtwoord = input("Wachtwoord (Minmaal 8 karakters, 1 hoofdletter en 1 cijfer): ")
            if len(wachtwoord) < 8:
                print("Wachtwoord moet minimaal 8 karakters bevatten.")
            elif re.search('[0-9]', wachtwoord) is None:
                print("Wachtwoord moet minimaal 1 cijfer bevatten.")
            elif re.search('[A-Z]', wachtwoord) is None:
                print("Wachtwoord moet minimaal 1 hoofdletter bevatten.")
            else:
                return wachtwoord
                print("Wachtwoord voldoet aan voorwaarden.")
                break


    goed_wachtwoord = wachtwoord(goed_wachtwoord)

if new_customer == 'ja':
    print("Om uw fiets te kunnen stallen dient u eerst in te loggen. Volg alstublieft de volgende stappen: \n")
    email = input('Vul hier uw e-mail in: ').lower()
    wachtwoord = input('Vul hier uw wachtwoord in: ')

cursor = db.cursor()
cursor.execute(
    'INSERT INTO user(first_name, insertion, last_name, zip, `number`, email, password) VALUES(%s, %s, %s, %s, %s, %s, %s)',
    (first_name, insertion, last_name, zip, number, goed_email, goed_wachtwoord))
db.commit()

print(cursor.rowcount, 'record inserted.\n')

db.close()

# verwijder dit maar
