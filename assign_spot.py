import datetime
import random
import db_connect

# Zorg dat dit bestand met het database bestand kan communniceren door de waarde te pakken uit het database bestand.
db = db_connect.db

# Defineer variabelen.
dateAndTime = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
ovnummer = "37:196:78:107"
plaatsenBezet = []
allePlaatsen = []

# Query om de correcte gebruiker te selecteren.
userQuery = "SELECT `userID` " \
            "FROM `user` " \
            "WHERE `ov` = '" + ovnummer + "'"

# Voer de query uit.
cursor = db.cursor()
cursor.execute(userQuery)

# Zet het resultaat van de query in een waarde.
data = cursor.fetchone()
for entry in data:
    result = entry

cursor.close()

# Query om bezette plaatsnummers te selecteren.
spotQuery = "SELECT `spot` " \
            "FROM `interaction`"

# Voer de query uit.
cursor = db.cursor()
cursor.execute(spotQuery)

# Zet het resultaat van de query in een lijst.
spot = list(cursor.fetchall())

# Zet de waardes van de query in een lijst.
for entry in spot:
    entries = list(entry)
    plaatsenBezet.append(entries)

# Maak een lijst met plaatsnummer van 1 tot en met 100.
for i in range(1, 101):
    allePlaatsen.append(i)

# Haal de bezette plaatsen uit de lijst met alle plaatsnummers
for numberList in plaatsenBezet:
    for number in numberList:
        allePlaatsen.remove(int(number))

# Zorg dat er een random plaats wordt toegewezen die nog niet bezet is.
while True:
    spotnummer = random.randrange(1, 101)

    if spotnummer in allePlaatsen:
        break

cursor.close()

# Query om de gebruiker en plaatsnummer in de database te zetten.
query2 = "INSERT INTO `interaction`(`userID`, `date`, `spot`) " \
         "VALUES ({}, '{}', {})".format(result, dateAndTime, spotnummer)
print(query2)
