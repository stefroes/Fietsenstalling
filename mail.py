# Hij stuurt nu emails op de localhost.
# Deze ontvang ik met het programma "Test Mail Server Tool".
# Als je dat programma download, dan kan je ook de mailfunctie testen.


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
import string

# Maak de headers aan voor de mail
msg = MIMEMultipart()
msg['From'] = "noreply@fietsenstalling.nl"
msg['To'] = "test@mail.com"
msg['Subject'] = "Testmail"

fiets_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

# Maak de body van de mail aan in HTML.
body = "<h2>Testbericht</h2>" \
       "Dit is een testbericht. <br>" \
       "Hier is de fiets code: <br>" \
       + fiets_code + "<br>" \
                      "Met vriendelijke groeten, <br>" \
                      "NS Fietsenstalling"

msg.attach(MIMEText(body, 'html'))

# Maak verbinding mer de SMTP Email dienst en verstuur de email. Misschien nog gegevens aanpassen als het live is?
server = smtplib.SMTP("localhost", 25)
server.connect("localhost", 25)
# server.starttls()
server.ehlo()
# server.login('email', 'password')
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
