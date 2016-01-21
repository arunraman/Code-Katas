#!/usr/bin/python

import re

string = "CountryCode=%(c)s,LocalAreaCode=%(l)s,Number=%(n)s"

num_lines = int(raw_input())

for i in xrange(num_lines):
    a = re.findall(r"[^\W\d_]+|\d+", raw_input())
    line = re.split("\W+", raw_input())
    print string % {'c': line[0], 'l': line[1], 'n': line[2]}
