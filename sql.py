import mysql.connector


# --- MYSQL INSTALLEREN
# GA NAAR FILE -> SETTINGS -> PROJECT -> PROJECT INTERPRETER -> KLIK RECHTS OP HET PLUS ICON
# ZOEK NAAR 'mysql-connector', KIES DEZE EN KLIK OP 'Install Package'


# --- INLOGGEN OP DATABASE
# https://roeswebdesign.nl:8443/domains/databases/phpMyAdmin/
# username: fietsen_user
# password: QYm6Pt3Cv4cDNynT
print("Welkom bij de NS - fietsenstalling.\n")

new_customer = input('Heeft u al een account bij de NS-fietsenstalling? Type ja of nee: ')

if new_customer == 'nee' or 'Nee':
    print('\nOm uw fiets te kunnen stallen in de NS-fietsenstalling dient u eerst een account aan te maken.\n')
    first_name = input('Vul hier uw voornaam in: ').capitalize()
    insertion = input('Vul hier uw tussenvoegsels in: ')
    last_name = input('Vul hier uw achternaam in: ').capitalize()
    zip = input('Vul hier uw postcode in: ').replace(' ', '').upper()
    number = input('Vul hier uw huisnummer in: ')
    email = input('Vul hier uw e-mail in: ').lower()



db = mysql.connector.connect(
    host='37.97.240.38',
    user='fietsen_user',
    passwd='QYm6Pt3Cv4cDNynT',
    database='fietsenstalling'
)

cursor = db.cursor()
cursor.execute('INSERT INTO user(first_name, insertion, last_name, zip, number, email) VALUES(%s, %s, %s, %s, %s, %s)', (first_name, insertion, last_name, zip, number, email))
db.commit()

print(cursor.rowcount, 'record inserted.\n')

if cursor.rowcount == 1:
    print("Om uw fiets te kunnen stallen, dient u eerst in te loggen. Volg alstublieft de volgende stappen:\n")

db.close()

