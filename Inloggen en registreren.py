# Registratie voor nieuwe gebruikers
# Input veld: Voor + achternaam
# Input veld: Postcode + huisnummer
# “Huidige datum”
# Input veld: Email
# Input veld: wachtwoord
# Input veld: wachtwoord (controle)
# Pincode (4 cijfers)
# Captcha
# label uitprinten voor op je fiets(dit is je unieke code)
#
# Inlogsysteem voor al bestaande gebruikers
# Input veld: Email
# Input veld: Wachtwoord
# Knop fiets ophalen, wegzetten of informatie opvragen.

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

email = str(input('Email: '))

import re

def wachtwoord():
    while True:
        wachtwoord = input("Wachtwoord (Minmaal 8 karakters, 1 hoofdletter en 1 cijfer): ")
        if len(wachtwoord) < 8:
            print("Wachtwoord moet minimaal 8 karakters bevatten.")
        elif re.search('[0-9]',wachtwoord) is None:
            print("Wachtwoord moet minimaal 1 cijfer bevatten.")
        elif re.search('[A-Z]',wachtwoord) is None:
            print("Wachtwoord moet minimaal 1 hoofdletter bevatten.")
        else:
            print("Wachtwoord voldoet aan voorwaarden.")
            break
        return str(wachtwoord)
wachtwoord()
# wachtwoord_check = str(input('Herhaal wachtwoord: '))
def wachtwoord_check():
    while True:
        if wachtwoord_check != wachtwoord():
            print("Dit moet gelijk zijn aan je wachtwoord.")
        else:
            print("Wachtwoord is set")
            break

wachtwoord_check()
# if wachtwoord_check != wachtwoord:
#     print()

pincode = input('4 cijferige pincode: ')

# Captcha
# label uitprinten voor op je fiets(dit is je unieke code)

#inloggen
#
# email_inlog = input('Voer uw e-mail in')
# wachtwoord_inlog = input('Voer uw wachtwoord in')

# Knop fiets ophalen, wegzetten of informatie opvragen.


registratie = [voornaam, achternaam, postcode, huisnummer, datum_datum, datum_tijd, email, wachtwoord, pincode]

print(registratie)

