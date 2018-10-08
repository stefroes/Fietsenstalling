# Als je mailen wilt op de localhost, download het programma "Test Mail Server Tool".
# Als je dat programma download, dan kan je ook de mailfunctie testen.

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
import string

# Maak het object bericht aan.
msg = MIMEMultipart()

# Genereer de random fietscode met getallen en letters van 5 (k=5) tekens
fiets_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

# Maak de bericht van de mail aan in HTML.
message = "<h2>Testbericht</h2>" \
          "Dit is een testbericht. <br>" \
          "Hier is de fiets code: <br>" \
          + fiets_code + "<br>" \
                         "Met vriendelijke groeten, <br>" \
                         "NS Fietsenstalling"

# Maak de parameters van het bericht aan.
password = "identificatiesysteem"
msg['From'] = "fietsenstallingv1a@gmail.com"
msg['To'] = "jellevandenbroek@gmail.com"
msg['Subject'] = "Subscription"

# Voeg het bericht toe aan de mail
msg.attach(MIMEText(message, 'plain'))

# Maak verbinding met de gmail server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Stuur login naar gmail om de mail te kunnen verzenden
server.login(msg['From'], password)

# Stuur de email via de server
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("successfully sent email to %s:" % (msg['To']))

# Code om lokaal emails te sturen
# smtpObj = smtplib.SMTP('localhost')
# smtpObj.sendmail(msg['From'], msg['To'], msg.as_string())
# print("Successfully sent email")
