import mysql.connector

# Maak verbinding met de database
db = mysql.connector.connect(
    host='37.97.240.38',
    user='fietsen_user',
    passwd='QYm6Pt3Cv4cDNynT',
    database='fietsenstalling',
    buffered=True
)
