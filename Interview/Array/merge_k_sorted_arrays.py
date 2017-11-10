import heapq

def addtoheap(result, it, i):
    try:
        heapq.heappush(result, (next(it), i))
    except StopIteration:
        pass

def mergeksortedarrays(lists):
    its = map(iter, lists)
    result = []
    for i, it in enumerate(its):
        # Each Iter is mapped to the 2D array index
        addtoheap(result, it, i)
    while result:
        res, i = heapq.heappop(result)
        addtoheap(result, its[i], i)
        yield res

for x in mergeksortedarrays([[1, 3, 5], [2, 4, 6], [7, 8, 9], [10]]):
    print x