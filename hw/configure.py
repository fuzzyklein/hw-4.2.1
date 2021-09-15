from configparser import ConfigParser
from os import environ, sep
from pathlib import Path

from globals import BASEDIR

CONFIG_FILE = BASEDIR / ('etc' + sep + 'hw.conf')

class Configure(dict):
    def __init__(self, file=None):
        super().__init__()
        try:
            if not file: file = CONFIG_FILE
            parser = ConfigParser()
            parser.read_string('[DEFAULT]\n' + Path(file).read_text())
        except FileNotFoundError:
            parser.read_string("""[DEFAULT]
program = hw
version = 4.2.1

args_json_file = etc/arguments.json
epilog = etc/epilog.txt

logfile = log/hw.log

""")
        self |= parser['DEFAULT']
