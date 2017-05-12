import random

servers = ['A', 'B', 'C', 'D']
weight = [10, 2, 8, 11]
my_list = []
sum = 0
if len(servers) == len(weight):
    for i in xrange(len(servers)):
        sum += weight[i]
        my_list += [servers[i]] * weight[i]

print my_list[random.randint(0, sum-1)]