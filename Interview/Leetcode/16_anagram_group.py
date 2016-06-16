import itertools

words = ['abc', 'cab', 'cafe', 'goo', 'face', 'ogo']
output = []
for key, group in itertools.groupby(sorted(words), sorted):
    output.append(list(group))
print output
