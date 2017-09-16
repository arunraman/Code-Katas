from heapq import heappop, heappush

# class MedianFinder:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.lower_heap = []
#         self.upper_heap = []
#
#     def addNum(self, num):
#         """
#         Adds a num into the data structure.
#         :type num: int
#         :rtype: void
#         """
#         # Balance smaller half and larger half.
#         if not self.lower_heap or num > -self.lower_heap[0]:
#             heappush(self.upper_heap, num)
#             if len(self.upper_heap) > len(self.lower_heap) + 1:
#                 heappush(self.lower_heap, -heappop(self.upper_heap))
#         else:
#             heappush(self.lower_heap, -num)
#             if len(self.lower_heap) > len(self.upper_heap):
#                 heappush(self.upper_heap, -heappop(self.lower_heap))
#
#         print self.lower_heap, self.upper_heap
#
#
#     def findMedian(self):
#         """
#         Returns the median of current data stream
#         :rtype: float
#         """
#         if len(self.upper_heap) == len(self.lower_heap):
#             return (-self.lower_heap[0] + self.upper_heap[0]) / 2.0
#         else:
#             return self.upper_heap[0]

from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


SM = MedianFinder()
SM.addNum(2)
print SM.findMedian()
SM.addNum(3)
print SM.findMedian()
SM.addNum(6)
print SM.findMedian()
SM.addNum(10)
print SM.findMedian()
SM.addNum(4)
SM.addNum(100)
print SM.findMedian()
