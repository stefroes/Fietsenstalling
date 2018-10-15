import hashlib


def compute_md5_hash(my_string, dateandtime):
    """Maak een MD5 hash van de input."""
    m = hashlib.md5()
    # Maak een MD5 hash van de code van de gebruiker en de huidige tijd.
    m.update(my_string.encode('utf-8') + str(dateandtime).encode('utf-8'))
    return m.hexdigest()
