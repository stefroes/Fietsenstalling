from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_mail(name, tomail, fiets_code):
    """ Functie om email op te stellen en te versturen. """
    # Maak het object bericht aan.
    msg = MIMEMultipart()

    # Maak de bericht van de mail aan in HTML.
    message = "Beste {},<br><br>" \
              "Bedankt voor het gebruiken van onze fietsenstalling.<br>" \
              "Hier is uw fiets code: <br>" \
              "<h1>{}</h1>" \
              "Deze code heeft u nodig om uw fiets uit te checken, bewaar deze code daarom goed ! <br>" \
              "   <br>    "\
              "Met vriendelijke groeten, <br>" \
              "NS Fietsenstalling".format(name, fiets_code)

    # Maak de parameters van het bericht aan.
    password = "identificatiesysteem"
    msg['From'] = "fietsenstallingv1a@gmail.com"
    msg['To'] = tomail
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
