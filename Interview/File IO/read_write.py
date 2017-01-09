import os, re

def read_1(file):
    with open(file) as F:
        print "Opening ", F.name
        print F.seek(0,2)
        for line in F.readlines():
            match = re.match(r'(\d+ +\w +\d\.\d+)', line)
            if match:
                print match.group(1)


if os.path.exists("read1.txt"):
    read_1("read1.txt")