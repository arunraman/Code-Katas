#!/usr/bin/python

from collections import defaultdict, Counter
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
                remove_punctuation = re.compile(r'([^A-Za-z0-9])')
                remove_punctuation.sub("", word)
                word_dict[word] += 1
    print word_dict


def Main():
    #if not os.path.exists(sys.argv[1]):
    #    sys.exit("Please specify a file name for word count")

    #word_count(sys.argv[1])

    # Clever way to do it ;)
    words = re.findall(r'\w\.\w\.?|\w+', open('hash_test.txt').read().lower())
    count = Counter(words).most_common(5)
    print count

Main()
