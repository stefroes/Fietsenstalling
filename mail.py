# Hij stuurt nu emails op de localhost.
# Deze ontvang ik met het programma "Test Mail Server Tool".
# Als je dat programma download, dan kan je ook de mailfunctie testen.


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Maak de headers aan voor de mail
msg = MIMEMultipart()
msg['From'] = "noreply@fietsenstalling.nl"
msg['To'] = "test@mail.com"
msg['Subject'] = "Testmail"

# Maak de body van de mail aan in HTML
body = "<h2>Testbericht</h2>" \
       "Dit is een testbericht<br>" \
       "Dit is een test!"
msg.attach(MIMEText(body, 'html'))
# print(msg)

# Maak verbinding mer de SMTP Email dienst en verstuur de email
server = smtplib.SMTP("localhost", 25)
server.connect("localhost", 25)
# server.starttls()
server.ehlo()
# server.login('email', 'password')
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
