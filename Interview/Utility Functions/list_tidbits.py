#!/usr/bin/python
import collections
from operator import itemgetter


def filter(x):
    return x >= 'B'


def expressions(x):
    return '(%s)' % x

alpha_list = ['A', 'B', 'C']

new_list = []
for i in alpha_list:
    if filter(i):
        new_list.append(expressions(i))


# Read statements, left to right
print [expressions(i) for i in alpha_list if filter(i)]

# 2
num_list = [20, 40, 60]

print ['%s-%d' % (x, y) for x in alpha_list for y in num_list]

print [['%s-%d' % (x, y) for x in alpha_list] for y in num_list]

d = {'Arun': 10, 'Divya': 2, 'Vijay': 4}
od = collections.OrderedDict(sorted(d.items()))
data = {100: 'Vijay', 2: 'Divya', 50: 'Arun'}
d = collections.OrderedDict(sorted(data.items(), key=itemgetter(1)))
for k, v in zip(d.iteritems(), od.iteritems()):
    print k, v
