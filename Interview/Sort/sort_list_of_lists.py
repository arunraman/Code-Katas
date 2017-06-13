import operator
L=[[0, 1, 'f'], [10, 2, 't'], [9, 4, 'afsd']]
L.sort(key=operator.itemgetter(2))
print L