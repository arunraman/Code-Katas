import itertools

alphabets = ['A', 'B', 'C', 'D', 'E']
numbers = [1, 2, 3, 4, 5]
print list(itertools.chain(alphabets, numbers[::-1]))
for i in itertools.count(10, 0.25):
    if i < 20:
        print i
    else:
        break
print list(itertools.compress(alphabets, numbers))
print list(itertools.imap(None, alphabets, numbers))
for i in itertools.islice(itertools.count(), 5):
    print i

for i in xrange(0, 100, 10):
    print i
