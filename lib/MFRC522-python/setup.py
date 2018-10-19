from setuptools import setup

requirements = ['spidev>=3.2']
dependency_links = []
# We need to bring a GPIO library, which will be platform dependent
# Platform determining code uses /proc/cpuinfo, based on
# https://github.com/rec/echomesh/blob/master/code/python/echomesh/base/Platform.py
import platform

PLATFORM = platform.system().lower()

DEBIAN = 'debian'
MAC = 'darwin'
RASPBERRY_PI = 'raspberry-pi'
CHIP = 'c.h.i.p.'
UBUNTU = 'ubuntu'
WINDOWS = 'windows'

IS_LINUX = (PLATFORM == 'linux')

if IS_LINUX:
    PLATFORM = platform.linux_distribution()[0].lower()
    if PLATFORM == DEBIAN:
        try:
            with open('/proc/cpuinfo') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('Hardware'):
                        if "BCM2708" in line:
                            PLATFORM = RASPBERRY_PI
                            break
                        elif "Allwinner" in line:
                            PLATFORM = CHIP
                            break
        except:
            pass

GPIO_MAP = {
    RASPBERRY_PI: ("RPI.GPIO>=0.6", None),
    CHIP: ("CHIP_IO>=0.0.7", "git+https://github.com/xtacocorex/CHIP_IO.git#egg=chip_io-0.0.9"),
}

gpio_library = GPIO_MAP.get(PLATFORM)
if gpio_library is None:
    WARNING = '\033[1m\033[91m'
    ENDC = '\033[0m'
    print WARNING + "Warning: could not identify platform, so cannot import GPIO Library." + ENDC
else:
    requirement, dependency_link = gpio_library
    requirements.append(requirement)
    if dependency_link:
        dependency_links.append(dependency_link)

print "Also need to install: ", requirements, dependency_links
setup(name='MFRC522',
  version='0.8.3',
  packages=['MFRC522'],
  install_requires=requirements,
  dependency_links=dependency_links,
)
