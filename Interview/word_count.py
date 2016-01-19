#!/usr/bin/python

from collections import defaultdict
import sys
import os
import re


def word_count(file):
    word_dict = defaultdict(int)
    with open(file) as F:
        lines = F.readlines()
        for line in lines:
            line = line.rstrip()
            words = line.split()
            for word in words:
                word = word.lower()
                punct = re.compile(r'([^A-Za-z0-9])')
                punct.sub("", word)
                word_dict[word] += 1
    print word_dict


def Main():
    if not os.path.exists(sys.argv[1]):
        sys.exit("Please sepcify a file name for word count")

    word_count(sys.argv[1])

if __name__ == '__main__':
    Main()
