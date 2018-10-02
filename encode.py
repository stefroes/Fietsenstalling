import hashlib
import datetime


def compute_md5_hash(my_string):
    """Maak een MD5 hash van de input."""
    m = hashlib.md5()
    # Maak een MD5 hash van de code van de gebruiker en de huidige tijd.
    m.update(my_string.encode('utf-8') + str(datetime.datetime.now().strftime("%H:%M:%S")).encode('utf-8'))
    return m.hexdigest()


# TODO op de plek van "codehier", plaats de code van de gebruiker
print(compute_md5_hash("codehier"))
