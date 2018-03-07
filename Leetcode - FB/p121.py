class p121(object):
    def maxProfit(self, nums):
        minPrice, maxProfit = float("inf") , 0
        for price in nums:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit

S = p121()
print S.maxProfit([7, 1, 5, 3, 6, 4])
print S.maxProfit([7, 6, 4, 3, 1])