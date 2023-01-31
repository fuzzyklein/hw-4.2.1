"""Run the program."""

from pprint import pp
import sys

from hw.driver import Driver
from hw.hw import HelloWorld

if __name__ == '__main__':
    if {'-t', '--testing'}.intersection(sys.argv):
        Driver().run()
    else:
        HelloWorld().run()
