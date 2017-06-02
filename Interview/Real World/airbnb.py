class Solution(object):
    def hostsScheduling(self, nights_requested):
        return self.findmaxDays(nights_requested, 0)

    def findmaxDays(self, nights, index):
        if (index == len(nights) - 1):
            return nights[len(nights) - 1]
        if (index > len(nights) - 1):
            return 0
        return max(nights[index] + self.findmaxDays(nights, index + 2),
                   nights[index] + self.findmaxDays(nights, index + 3))


S = Solution()
print S.hostsScheduling([12,2,10,1])
print S.hostsScheduling([5,1,2,6,20,2])