from glob import glob
import logging
import os
from os import environ, listdir, makedirs
from pathlib import Path
from pprint import pprint as pp
import sys

from ansicolortags import printc

from arguments import Arguments
from configure import Configure
from environment import Environment
from globals import *
from tools import invisible

class Program():
    def __init__(self, settings=None):

        args = Arguments()
        conf = Configure(args['config'])
        env = Environment()
        self.settings = conf | env | args

        if __debug__:
            printc('<yellow>Program settings<reset>:')
            pp(self.settings)
            print()

        self.log = self.startlog()
        self.log.debug(f"Debugging {PROGRAM}")

    def startlog(self):
        if self.settings['log'] or 'logfile' in self.settings.keys():
            p = Path(self.settings['log'] if self.settings['log'] else self.settings['logfile'])
            # print(f'{__debug__=}')
            if __debug__:
                printc(f'<cyan>Log file<reset>: {p.name}')
                print()

            if not p.exists():
                if not p.parent.exists():
                    makedirs(p.parent)
                p.touch()
        else:
            p = None

        if __debug__:
            level = logging.DEBUG
        elif self.settings['verbose']:
            level = logging.INFO
        else:
            level = logging.WARNING

        logging.basicConfig(filename=str(p) if p else None, level=level, filemode='w')
        logging.captureWarnings(True)
        return logging.getLogger(__name__)

    def run(self):
        
        for f in filter(lambda s: self.settings["all"] or not invisible(s), self.settings["args"]):
            for name in glob(f, recursive=self.settings["recursive"]):
                self.process_fname(name)

    def process_fname(self, s):
        self.log.debug(f"Processing {s}...")
        p = Path(s)
        if not p.exists():
            if self.settings["verbose"]:
                print(f"File {s} does not exist.")
            return
        elif p.is_symlink():
            self.process_link(p)
        elif p.is_dir():
            self.process_dir(p)
        elif p.is_file():
            self.process_file(p)

    def process_link(self, p):
        if self.settings["follow"]:
            process_file(p)
        else:
            self.log.info(f"File {str(p)} is a symbolic link.")

    def process_dir(self, p):
        self.log.info(f"Processing directory {str(p)}")
        if self.settings["recursive"]:
            for f in listdir(str(p)):
                self.process_fname(os.path.join(str(p), f))

    def process_file(self, p):
        self.log.debug(f"{PROGRAM} is processing file {p}")
        if self.settings["verbose"]:
            print(f"Processing file {str(p)}.")
