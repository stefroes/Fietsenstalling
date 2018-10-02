import http.client
import urllib
import datetime

message = 'U heeft zojuist uw fiets opgehaald om ' + str(datetime.datetime.now().strftime("%H:%M:%S"))

print(message)

conn = http.client.HTTPSConnection('api.pushover.net:443')
conn.request('POST', '/1/messages.json',
             urllib.parse.urlencode({
                 'token': 'ajvm347bjn5o73ubkj3tzxkywgvbyi',
                 'user': 'uhkh497h942ogr4efpqsq78ahti2qj',
                 'message': message,
             }), {'Content-type': 'application/x-www-form-urlencoded'})
conn.getresponse()
