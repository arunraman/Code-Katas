from Interval import Interval

class p057(object):
    def insetInterval(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left, right = [], []
        for i in intervals:
            if i.end < s:
                left.append(i)
            elif i.start > e:
                right.append(i)
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return left + [Interval(s, e)] + right

S = p057()
print S.insetInterval([Interval(1, 3), Interval(6, 9)], Interval(2, 5))
print S.insetInterval([Interval(1, 2), Interval(3, 5), Interval(6, 7),
                       Interval(8, 10), Interval(12, 16)],
                      Interval(4, 9))