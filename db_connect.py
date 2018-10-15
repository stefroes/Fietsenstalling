import mysql.connector

# Maak verbinding met de database


try:
    db = mysql.connector.connect(
        host='37.97.240.38',
        user='fietsen_user',
        password='QYm6Pt3Cv4cDNynT',
        database='fietsenstalling',
        buffered=True,
        raise_on_warnings=True
    )
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
