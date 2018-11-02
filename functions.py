import ctypes

def is_high_resolution():
    """Check if is high resolution screen for better font rendering"""
    user32 = ctypes.windll.user32
    screen = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
    return screen[0] >= 3840 and screen[1] >= 2160


def clean(string, capitalize=True, remove_spaces=True, lowercase=False, uppercase=False):
    """Format a string for clean output"""
    if capitalize:
        string = string.capitalize()
    elif lowercase:
        string = string.lower()
    elif uppercase:
        string = string.upper()
    if remove_spaces:
        string = string.replace(' ', '')

    return string
