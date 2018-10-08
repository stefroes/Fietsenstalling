from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
import string


def send_mail():
    """ Functie om email op te stellen en te versturen. """
    # Maak het object bericht aan.
    msg = MIMEMultipart()

    # Genereer de random fietscode met getallen en letters van 5 (k=5) tekens
    fiets_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    # Maak de bericht van de mail aan in HTML.
    message = "Beste klant,<br><br>" \
              "Bedankt voor het gebruiken van onze fietsenstalling.<br>" \
              "Hier is uw fiets code: <br>" \
              "<h1>" + fiets_code + "</h1><br>" \
                                    "Met vriendelijke groeten, <br>" \
                                    "NS Fietsenstalling"

    # Maak de parameters van het bericht aan.
    password = "identificatiesysteem"
    msg['From'] = "fietsenstallingv1a@gmail.com"
    msg['To'] = "jellevandenbroek@gmail.com"
    msg['Subject'] = "Fietsenstalling Fiets Code {}".format(fiets_code)

    # Voeg het bericht toe aan de mail
    msg.attach(MIMEText(message, 'HTML'))

    # # # Code om te mailen via gmail. # # #
    # Maak verbinding met de gmail server.
    server = smtplib.SMTP('smtp.gmail.com: 587')

    # Beveilig de mail bij het versturen.
    server.starttls()

    # Stuur login naar gmail om de mail te kunnen verzenden
    server.login(msg['From'], password)

    # Stuur de email via de server
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    # # # Code te mailen via localhost # # #
    # smtpObj = smtplib.SMTP('localhost')
    # smtpObj.sendmail(msg['From'], msg['To'], msg.as_string())

    # Als je mailen wilt op de localhost, comment dan het gmail gedeelte uit.
    # Download het programma "Test Mail Server Tool". Hiermee kun je de mailfunctie testen.


send_mail()
