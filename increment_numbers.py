"""USAGE: python increment_numbers.py FILENAME"""
import re
import sys

try:
    infilename = sys.argv[1]
except IndexError:
    print(__doc__, file=sys.stderr)
    sys.exit(1)

with open(infilename) as infile:
    for line in infile:
        print(re.sub(r'[0-9]+', lambda s: str(int(s.group(0)) + 1), line),
              end='')
