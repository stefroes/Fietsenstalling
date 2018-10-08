import http.client
import urllib
import datetime

# Maak een bericht aan om te sturen als notificatie.
message = 'U heeft zojuist uw fiets opgehaald om {}'.format(str(datetime.datetime.now().strftime("%H:%M:%S")))

# Maak verbinding met pushover.
conn = http.client.HTTPSConnection('api.pushover.net:443')
conn.request('POST', '/1/messages.json',
             urllib.parse.urlencode({
                 'token': 'ajvm347bjn5o73ubkj3tzxkywgvbyi',
                 'user': 'uhkh497h942ogr4efpqsq78ahti2qj',
                 'message': message,
             }), {'Content-type': 'application/x-www-form-urlencoded'})
conn.getresponse()

# User code Stef: uhkh497h942ogr4efpqsq78ahti2qj
# User code Jelle: uawn4pj4uk87kzjfkrfq4oxqsqd2pk
