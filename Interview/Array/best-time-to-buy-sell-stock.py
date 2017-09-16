#
# Say you have an array for which the ith element
# is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
#

def maxProfit(prices):
    max_profit, min_price = 0, float("inf")
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

print maxProfit([3, 2, 1, 4, 2, 5, 6])
print maxProfit([7, 6, 4, 3, 1])

# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).

def maxProfit2(prices):
    profit = 0
    for i in xrange(len(prices) - 1):
        profit += max(0, prices[i + 1] - prices[i])
    return profit

print maxProfit2([3, 2, 1, 4, 2, 5, 6])

#
# Design an algorithm to find the maximum profit.
# You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).

def maxProfit3(prices):
    hold1, hold2 = float("-inf"), float("-inf")
    release1, release2 = 0, 0
    for i in prices:
        release2 = max(release2, hold2 + i)
        hold2 = max(hold2, release1 - i)
        release1 = max(release1, hold1 + i)
        hold1 = max(hold1, -i)
    return release2

print maxProfit3([3, 2, 1, 4, 2, 5, 6])

# Design an algorithm to find the maximum profit. You may complete as
# many transactions as you like (ie, buy one and sell one share of the
# stock multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day.
# (ie, cooldown 1 day)
# Example:
#
# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]

def maxProfit4(prices):
    if not prices:
        return 0
    buy, sell, coolDown = [0] * 2, [0] * 2, [0] * 2
    buy[0] = -prices[0]
    for i in xrange(1, len(prices)):
        # Bought before or buy today.
        buy[i % 2] = max(buy[(i - 1) % 2], coolDown[(i - 1) % 2] - prices[i])
        # Sell today.
        sell[i % 2] = buy[(i - 1) % 2] + prices[i]
        # Sold before yesterday or sold yesterday.
        coolDown[i % 2] = max(coolDown[(i - 1) % 2], sell[(i - 1) % 2])
    return max(coolDown[(len(prices) - 1) % 2], sell[(len(prices) - 1) % 2])

print maxProfit4([3, 2, 1, 4, 2, 5, 6])
print maxProfit4([1, 2, 3, 0, 2])
