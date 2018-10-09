# Registratie

import datetime
import re

voornaam = input('Voornaam : ')
achternaam = input('Achternaam : ')

postcode = input('Postcode : ')
huisnummer = input('Huisnummer : ')

datum = str(datetime.datetime.now())
datum_vandaag = datum[:19]
datum_datum = datum[:10]
datum_tijd = datum[11:19]

goed_email = ''
def email(email):
    while True:
        email = str(input('Email: '))
        if re.search('[@]', email) is None:
            print("Voer een geldig email adres in.")
        elif re.search('[.]', email) is None:
            print("Voer een geldig email adres in.")
        else:
            print("Email voldoet aan voorwaarden")
            return email


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
            print("Wachtwoord voldoet aan voorwaarden.")
            return wachtwoord

goed_wachtwoord = wachtwoord(goed_wachtwoord)

# wachtwoord_check = str(input('Herhaal wachtwoord: '))
def wachtwoord_check():
    while True:
        wachtwoord_check = input('Herhaal wachtwoord: ')
        if wachtwoord_check != goed_wachtwoord:
            print("Dit moet gelijk zijn aan je wachtwoord.")
        else:
            print("Wachtwoord is set")
            break

wachtwoord_check()

goed_pincode = ''
def pincode(pincode):
    while True:
        pincode = input('4 cijferige pincode: ')
        if len(pincode) != 4:
            print("Wachtwoord moet 4 cijfers bevatten.")
        else:
            return pincode
            print("Pincode voldoet aan voorwaarden.")
            break

goed_pincode = pincode(goed_pincode)

# Captcha
# label uitprinten voor op je fiets(dit is je unieke code)

#inloggen
#
# email_inlog = input('Voer uw e-mail in')
# wachtwoord_inlog = input('Voer uw wachtwoord in')

# Knop fiets ophalen, wegzetten of informatie opvragen.


registratie = [voornaam, achternaam, postcode, huisnummer, datum_datum, datum_tijd, goed_email, goed_wachtwoord,
              goed_pincode]

print(registratie)
