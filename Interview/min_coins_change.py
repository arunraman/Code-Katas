"""
Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S.
Find the minimum number of coins the sum of which is S
(we can use as many coins of one type as we want),
or report that it's not possible to select coins in such a
way that they sum up to S.
"""
import sys


def min_coins_bottom_up(sum, v):
    if sum is None or sum <= 0:
        return False
    if v is None or len(v) < 1:
        return False

    minimum_coins = [sys.maxsize - 1 for i in xrange(sum + 1)]
    minimum_coins[0] = 0

    for i in xrange(0, len(v)):
        for j in xrange(1, sum + 1):
            if j >= v[i]:
                minimum_coins[j] = min(
                    minimum_coins[j],
                    minimum_coins[
                        j -
                        v[i]] +
                    1)

    return minimum_coins[sum]


def min_coins_top_down(total, coins, value_map):
    if (total == 0):
        return 0

    if total in value_map:
        return value_map[total]

    min = sys.maxsize

    for i in xrange(len(coins)):
        if coins[i] > total:
            continue
        val = min_coins_top_down(total - coins[i], coins, value_map)
        if (val < min):
            min = val

    if min != sys.maxsize:
        min += 1

    value_map[total] = min
    return min


sum = 9
v = [5, 10, 25]
value_map = {}
min_coins_bw_up = min_coins_bottom_up(sum, v)
min_coins_tp_dw = min_coins_top_down(sum, v, value_map)
if min_coins_bw_up == sys.maxsize - 1 and min_coins_tp_dw == sys.maxsize:
    print "Not able to get the exact change!"
else:
    print "Minimum Coins Bottom Up " + str(min_coins_bw_up) + \
          " Minimum Coins Top Down " + str(min_coins_tp_dw)
