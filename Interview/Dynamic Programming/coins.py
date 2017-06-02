# Coin Change Total Number of ways

# Same as Combination Sum 1 # If in doubt use the one you know and for the second part
# just do this min(combinationSum1(), key=len)

def coinchangetotalnumberofWays(coins, total):
    table = [0 for k in range(total + 1)]
    table[0] = 1

    for i in xrange(0, len(coins)):
        for j in xrange(coins[i], total + 1):
            table[j] += table[j - coins[i]]
    return table[total]


print coinchangetotalnumberofWays([1, 2, 3], 5)

# Minimum Number of Coins need for Total

def mincoinsNeeded(coins , total):
    # This how we do if else in list comprehension
    T = [float("inf") if m != 0 else 0 for m in xrange(total + 1)]
    R = [-1 for n in xrange(total + 1)]

    for i in xrange(0, len(coins)):
        for j in xrange(1, total + 1):
            if j >= coins[i]:
                if T[j] > 1 + T[j - coins[i]]:
                    T[j] = 1 + T[j - coins[i]]
                    R[j] = i
    print "Min Coins: " + str(T[total]) + " Coins: " + str(print_coins(R, coins))

def print_coins(R, coins):
    start = len(R) - 1
    res = []

    if R[start] == -1:
        print "No Solution Possible."
        return

    while start != 0:
        coin = coins[R[start]]
        res.append(coin)
        start = start - coin
    return res


mincoinsNeeded([7, 2, 3, 6], 13)

