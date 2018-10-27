from Crypto.Cipher import AES
import base64


def get_key():
    return '2qGZdeEHpbTiwFDkKvqC'


def encrypt(string):
    cipher = AES.new(get_key(), AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(string.rjust(32)))


def decrypt(string):
    cipher = AES.new(get_key(), AES.MODE_ECB)
    decoded = cipher.decrypt(base64.b64decode(string))
    return decoded.strip()


encrypted = encrypt('test')

