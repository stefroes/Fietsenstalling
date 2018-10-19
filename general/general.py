import ctypes


def check_high_resolution():
    """Check if is high resolution screen for better font rendering"""
    user32 = ctypes.windll.user32
    screen = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
    return screen[0] >= 3840 and screen[1] >= 2160


def valid_email():
    """Check if is valid e-mail"""
    # cursor = db.cursor()

    while True:
        string = input('E-mail: ').lower()

        # DIT KUT DING WERKT NIET GOED, GEEN FK IDEE WAAROM:
        # cursor.execute('SELECT count(userID) FROM `user` WHERE email = %s', string)

        if re.search('[@]', string) is None and len(string) > 5 and re.search('[.]', string) is None:
            print('Voer een geldig email adres in.')
        # elif cursor.fetchone()[0] > 0:
        #    print('Dit e-mail adres is al geregistreerd. Gebruik een andere pas of gebruik een ander e-mail adres.')
        else:
            return string


def valid_password():
    """Check if is valid password"""
    while True:
        string = input('Wachtwoord (Minmaal 8 karakters, 1 hoofdletter en 1 cijfer): ')
        if len(string) < 8:
            print('Wachtwoord moet minimaal 8 karakters bevatten.')
        elif re.search('[0-9]', string) is None:
            print('Wachtwoord moet minimaal 1 cijfer bevatten.')
        elif re.search('[A-Z]', string) is None:
            print('Wachtwoord moet minimaal 1 hoofdletter bevatten.')
        else:
            return string


def verify_password(string):
    """Verify two password to be the same"""
    while True:
        check = input('Herhaal wachtwoord: ')
        if check != string:
            print('Dit moet gelijk zijn aan je wachtwoord.')
        else:
            return string


def get_date():
    """Get current datetime"""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_code():
    """Generate a random code with 5 letters and numbers"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
