import itertools
input = [[1, 2, 3], [1], [1, 2]]
print [each for each in itertools.product(*input)]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [list(reversed(x)) for x in zip(*matrix)]