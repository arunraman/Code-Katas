class p123(object):
    def maxProfit(self, prices):
        hold1, hold2 = float("inf"), float("inf")
        release1, release2 = 0, 0