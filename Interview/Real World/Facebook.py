import os
from collections import defaultdict
from itertools import izip

dino_dict = defaultdict(list)

def parseCsv(filename):
    with open(filename) as F:
        line =  F.readline().strip().split(";")
        lines = F.readlines()
        for l in lines:
            l_2 = l.rstrip().split(";")
            for l_1, l_3 in izip(line, l_2):
                dino_dict[removeDoublequotes(l_1)].append(removeDoublequotes(l_3))

    print dino_dict

def removeDoublequotes(string):
    if string.startswith("\"") and string.endswith("\""):
        return string[1:-1]
    else:
        return string

def Main():
    if os.path.exists('dino.txt'):
        parseCsv('dino.txt')


Main()