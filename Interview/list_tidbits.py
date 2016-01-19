#!/usr/bin/python


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
