import itertools

words = ['abc', 'cab', 'cafe', 'goo', 'face']
output = []
for key, group in itertools.groupby(sorted(words, key=sorted), sorted):
    output.append(list(group))
print output
