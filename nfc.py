from lib import MFRC522
import mysql.connector
import RPi.GPIO as GPIO
import signal

database = {
    'host': '37.97.240.38',
    'user': 'fietsen_user',
    'passwd': 'QYm6Pt3Cv4cDNynT',
    'database': 'fietsenstalling'
}

#db = mysql.connector.connect(host=database['host'], user=database['user'], passwd=database['passwd'], database=database['database'])
#cursor = db.cursor()

db = mysql.connector.connect(
    host='37.97.240.38',
    user='fietsen_user',
    passwd='QYm6Pt3Cv4cDNynT',
    database='fietsenstalling'
)

continue_reading = True


# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()


# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print('SEARCHING: ')

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print 'Card detected'

    # Get the UID of the card
    (status, uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # 24:C4:4E:6B (OV: HEX)
        # 37:196:78:107 (OV: Decimale)

        ov = '{}:{}:{}:{}'.format(uid[0], uid[1], uid[2], uid[3])
        # email = raw_input("Vul uw e-mail: ").lower()

        print(ov)

        cursor = db.cursor()
        sql = "SELECT * FROM user WHERE ov = {}".format(ov)

        cursor.execute(sql)
        result = cursor.fetchall()

        for x in result:
            print(x)

db.close()
