from Interval import Interval

class p056(object):
    def mergeIntervals(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev , curr = result[-1], intervals[i]
            if curr.start <= prev.end:
                prev.end = max(prev.end, curr.end)
            elif curr.start == prev.end + 1:
                prev.end = max(prev.end, curr.end)
            else:
                result.append(curr)
        return result

S = p056()
print S.mergeIntervals([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)])
