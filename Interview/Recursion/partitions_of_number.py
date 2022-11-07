def partitions(n):
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return

    # modify partitions of n-1 to form partitions of n
    for p in partitions(n - 1):
        p.append(1)
        yield p
        p.pop()
        if p and (len(p) < 2 or p[-2] > p[-1]):
            p[-1] += 1
            yield p


for partition in partitions(5):
    print(partition)
