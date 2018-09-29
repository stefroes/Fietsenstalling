import mysql.connector


# --- MYSQL INSTALLEREN
# GA NAAR FILE -> SETTINGS -> PROJECT -> PROJECT INTERPRETER -> KLIK RECHTS OP HET PLUS ICON
# ZOEK NAAR 'mysql-connector', KIES DEZE EN KLIK OP 'Install Package'


# --- INLOGGEN OP DATABASE
# https://roeswebdesign.nl:8443/domains/databases/phpMyAdmin/
# username: fietsen_user
# password: QYm6Pt3Cv4cDNynT

Voornaam = str(input("Vul hier uw voornaam in: "))
Tussenvoegsels = str(input("Vul hier uw tussenvoegsels in: "))
Achternaam = str(input("Vul hier uw achternaam in: "))
Postcode = str(input("Vul hier uw postcode in:"))
Huisnummer = str(input("Vul hier uw huisnummer in: "))
Email = str(input("Vul hier uw Email in: "))

db = mysql.connector.connect(
    host='37.97.240.38',
    user='fietsen_user',
    passwd='QYm6Pt3Cv4cDNynT',
    database='fietsenstalling'
)

cursor = db.cursor()

cursor.execute(
    "INSERT INTO user(Voornaam, Tussenvoegsels, Achternaam, Postcode, Huisnummer, Email) VALUES("+Voornaam+", "+Tussenvoegsels+", "+Achternaam+", "+Postcode+", "+Huisnummer+", "+Email+")"
)
db.commit()
db.close()

