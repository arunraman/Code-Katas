def tableify(names, columns):
    rows = int(len(names) / columns) + (len(names) % columns > 0)
    result = [[] for _ in range(rows)]

    for i in xrange(len(names)):
        result[i % rows].append(names[i])
    return result


names = 'Adam Brett Cari Donna Ethan Fred Grok Han Izzy Jay'.split()
columns = 4

print str(tableify(names, columns)).replace(', [',",\n [")