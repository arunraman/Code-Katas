import os

def read_lines(F):
    for line in F:
        line = line.strip()
        if line.startswith('#'):
            continue
        if not line:
            continue
        yield line


if os.path.exists("read1.txt"):
    with open("read1.txt") as F:
        for line in read_lines(F):
            print line