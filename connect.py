import mysql.connector


def connect():
    """Connect to external database"""
    try:
        db = mysql.connector.connect(
            host='db4free.net',
            user='fietsen_user',
            password='QYm6Pt3Cv4cDNynT',
            database='fietsenstalling',
            buffered=True,
            raise_on_warnings=True
        )
        return db
    except mysql.connector.Error as err:
        print('Something went wrong: {}'.format(err))


db = connect()
