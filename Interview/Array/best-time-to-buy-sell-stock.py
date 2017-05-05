def maxProfit(prices):
    max_profit, min_price = 0, float("inf")
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

print maxProfit([3, 2, 1, 4, 2, 5, 6])
print maxProfit([7, 6, 4, 3, 1])