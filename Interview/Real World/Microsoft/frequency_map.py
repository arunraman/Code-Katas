import random

class Solution(object):
    def __init__(self):
        self.nums = [random.randint(1, 9) for i in xrange(100)]

    def getFrequency(self):
        i = 0
        while i < len(self.nums):
            if self.nums[i] <= 0:
                i += 1
                continue
            ind = self.nums[i] - 1
            if self.nums[ind] > 0:
                self.nums[i] = self.nums[ind]
                self.nums[ind] = -1

            else:
                self.nums[ind] -= 1
                self.nums[i] = 0
                i += 1

    def printFrequency(self):
        for i in range(0, 9):
            print 'Number of {}\'s : {}'.format(i + 1, abs(self.nums[i]))

S = Solution()
S.getFrequency()
S.printFrequency()