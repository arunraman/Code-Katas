import itertools
input = [[1, 2, 3], [1], [1, 2]]
print [each for each in itertools.product(*input)]