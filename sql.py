import mysql.connector


# --- MYSQL INSTALLEREN
# GA NAAR FILE -> SETTINGS -> PROJECT -> PROJECT INTERPRETER -> KLIK RECHTS OP HET PLUS ICON
# ZOEK NAAR 'mysql-connector', KIES DEZE EN KLIK OP 'Install Package'


# --- INLOGGEN OP DATABASE
# https://roeswebdesign.nl:8443/domains/databases/phpMyAdmin/
# username: fietsen_user
# password: QYm6Pt3Cv4cDNynT


db = mysql.connector.connect(
    host='37.97.240.38',
    user='fietsen_user',
    passwd='QYm6Pt3Cv4cDNynT',
    database='fietsenstalling'
)

cursor = db.cursor()

cursor.execute(
    "INSERT INTO user(voornaam) VALUES('laurens')"
    "INSERT INTO user(tussenvoegsels) Values('van de')"
    "INSERT INTO user(achternaam) VALUES('Hulst')"
    "INSERT INTO user(postcode) VALUES('7313BR')"
    "INSERT INTO user(huisnummer) VALUES('15')"
    "INSERT INTO user(email) VALUES('laurensvandehulst@gmail.com')"
)
db.commit()
db.close()

# ben wezen zoeken naar iets om dit:
#FirstName = str(input("Vul hier uw voornaam in: "))
#LastName = str(input("Vul hier uw achternaam in: "))
#Adress = (input("Vul hier uw postcode in: "))
#Huisnummer = eval(input("Vul hier uw huisnummer in:"))
#Email = str(input("Vul hier uw email in: "))
#in te linken aan de waarden bij "cursor.execute() maar krijg het niet voor elkaar. Misschien kan een van jullie het?
