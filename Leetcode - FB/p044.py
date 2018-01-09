class p044(object):
    def wildcardMatching(self, s, p):
        dp = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]

        dp[0][0] = True

        for i in xrange(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]

        for i in xrange(1, len(s) + 1):
            dp[i][0] = False
            for j in xrange(1, len(p) + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
                else:
                    dp[i][j] = dp[i][j -1] or dp[i - 1][j]

        return dp[len(s)][len(p)]


S = p044()
print S.wildcardMatching("aa", "a")