#!/usr/bin/python

import json
import sys
import math
import collections

x_1 = sys.argv[1]
y_1 = sys.argv[2]

distance = collections.defaultdict(dict)
with open('cordinates.json') as data_file:
    data = json.load(data_file)

for d in data:
    a, b = d["value"].split(",")
    x_2 = int(a)
    y_2 = int(b)
    x_diff = math.pow(x_2, 2) + math.pow(int(x_1), 2) - (2 * x_2 * int(x_1))
    y_diff = math.pow(y_2, 2) + math.pow(int(y_1), 2) - (2 * y_2 * int(y_1))
    distance[str(d["id"])] = math.sqrt(x_diff + y_diff)

print sorted(distance, key=distance.get)
