def isMatchDP(s, p):
    m = len(s)
    n = len(p)

    if n == 0 and m == 0:
        return True
    if n == 0 and m != 0:
        return False
    if p.count('*') == len(p):
        return True
    if len(p) - p.count('*') > m:
        return False

    dp = [True] + [False] * m
    for cp in p:
        if cp != '*':
            for i in xrange(m, 0, -1):  # m, m-1, .. 1
                dp[i] = dp[i - 1] and (cp == '?' or s[i - 1] == cp)
        else:
            for i in xrange(1, m + 1):
                dp[i] = dp[i] or dp[i - 1]
        dp[0] = dp[0] and cp == '*'

    return dp[m]

print isMatchDP("aaasda", "*a?*")