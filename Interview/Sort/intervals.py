class Interval():
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)

import heapq
class Solution():

    def __init__(self):
        self.__intervals = []

    def addNum(self, val):
        heapq.heappush(self.__intervals, (val, Interval(val, val)))

    # Data Stream as an disjoint intervals
    def getIntervals(self):
        stack = []
        while self.__intervals:
            idx, cur = heapq.heappop(self.__intervals)
            if not stack:
                stack.append(cur)
            else:
                prev = stack[-1]
                if prev.end + 1 >= cur.start:
                    prev.end = max(prev.end, cur.end)
                else:
                    stack.append(cur)
        self.__intervals = stack
        print self.__intervals


    def Mergeintervals(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        # [1, 3]-> Previous , [2, 6] -> Current
        # compare and squeeze
        for i in xrange(1, len(intervals)):
            prev, current = result[-1], intervals[i]
            if current.start <= prev.end:
                prev.end = max(prev.end, current.end)
            elif current.start == prev.end + 1:
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
        return result

    def IsOccupied(self, intervals, interval_check):
        if not intervals:
            return False
        for i in xrange(len(intervals)):
            if interval_check.start >= intervals[i].start and interval_check.end <= intervals[i].end:
                return True
        return False

    def removeOverlappingInterval(self, intervals):
        # [1, 2], [2, 3], [3, 4], [1, 3] remove [1, 3]
        if not intervals:
            return intervals
        intervals.sort(key = lambda x: x.start)
        result, prev, final, removed = 0, 0, [], []
        for i in xrange(1, len(intervals)):
            current, previous = intervals[i], intervals[prev]
            if current.start < previous.end: # this proves there is a overlap
                if current.end < previous.end:
                    prev = i
                result += 1
                final.append(previous)
                removed.append(current)
            else:
                prev = i
                final.append(current)
        print "Number  of Overlaps = {} \nFinal Intervals = {} \nRemoved Intervals = {}".format(result, final, removed)



S = Solution()
print S.Mergeintervals([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)])
M_I = S.Mergeintervals([Interval(1, 3), Interval(4, 10), Interval(20, 30)])
print M_I
print S.IsOccupied(M_I, Interval(20, 30))
S.removeOverlappingInterval([Interval(1, 2), Interval(2, 3), Interval(3, 4), Interval(1 ,3)])
S.addNum(1)
S.addNum(3)
S.addNum(7)
S.addNum(2)
S.addNum(6)
S.getIntervals()



