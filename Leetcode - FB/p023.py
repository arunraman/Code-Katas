import heapq


class p023(object):
    def mergeksortedLists(self, nums):
        its = map(iter, nums)
        result = []
        for i, it in enumerate(its):
            self.addtoHeap(result, it, i)
        while (result):
            res, i = heapq.heappop(result)
            self.addtoHeap(result, its[i], i)
            yield res

    def addtoHeap(self, result, it, i):
        try:
            heapq.heappush(result, (next(it), i))
        except StopIteration:
            pass


S = p023()
for x in S.mergeksortedLists([[1, 3, 5], [2, 4, 6], [7, 8, 9], [10]]):
    print x
