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

cursor.execute('SELECT name FROM user')

result = cursor.fetchall()

for i in result:
    print(i)



