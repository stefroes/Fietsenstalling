import re
import db_connect
import random
import string
import datetime
import encode
import mail


# Zorg dat dit bestand met het database bestand kan communniceren door de waarde te pakken uit het database bestand.
db = db_connect.db

# --- MYSQL INSTALLEREN
# GA NAAR FILE -> SETTINGS -> PROJECT -> PROJECT INTERPRETER -> KLIK RECHTS OP HET PLUS ICON
# ZOEK NAAR 'mysql-connector', KIES DEZE EN KLIK OP 'Install Package'


# --- INLOGGEN OP DATABASE
# https://www.db4free.net/phpMyAdmin/db_structure.php?server=1&db=fietsenstalling
# username: fietsen_user
# password: QYm6Pt3Cv4cDNynT

while True:
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
            """ Controleer of het ingevulde email adres voldoet aan de eisen. """
            while True:
                email = str(input('Vul hier uw Email in: '))
                if re.search('[@]', email) is None:
                    print("Voer een geldig email adres in.")
                elif re.search('[.]', email) is None:
                    print("Voer een geldig email adres in.")
                else:
                    print("Email voldoet aan voorwaarden")
                    return email


        # Pak de huidige datum en tijd
        dateAndTime = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        # Genereer de random fietscode met getallen en letters van 5 (k=5) tekens
        fiets_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

        while True:
            goed_email = email(email)

            cursor = db.cursor()
            query = "INSERT INTO user(unique_code, first_name, insertion, last_name, zip, `streetnumber`, email, date_time) " \
                    "VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(fiets_code, first_name, insertion,
                                                                                    last_name, zip, number,
                                                                                    goed_email, dateAndTime)
            try:
                cursor.execute(query)
                db.commit()
                break
            except:
                print('Er is al een gebruiker met uw gegevens.')

        mail.send_mail(first_name, goed_email, fiets_code)

        print(query)

        db.close()
        break
    elif new_customer == 'ja':
        print("Om uw fiets te kunnen stallen dient u eerst in te loggen. Volg alstublieft de volgende stappen: \n")
        email = input('Vul hier uw e-mail in: ').lower()
        break
    else:
        print("Voer een geldige waarde in.")

# TODO Maak email inhoud beter
# TODO Deel de bestanden op in inchecken en uitchecken.
# TODO Maak een informatiepagina met algemene en persoonlijke informatie.
# TODO Lezen van OV code, in een waarde stoppen en aan gebruiker koppelen in database.
# TODO Beslissen wat er moet gebeuren met de gebruiker als de fiets is geparkeerd.
# TODO Zorg ervoor dat fietscode uniek is.
# TODO Maak een inlog systeem - Suhaib
# TODO Zorg ervoor dat email uniek is en dat er een melding komt als dit niet zo is.
# TODO Misschien if statements optimaliseren volgens beoordelingsformulier PROG.
# TODO Commentaar toevoegen aan functies met """ ... """ en bij overige dingen met # ... .
