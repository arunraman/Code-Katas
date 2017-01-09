class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for x in range(m)]
        dp[0][0] = 1
        for x in range(m):
            for y in range(n):
                if x + 1 < m:
                    dp[x + 1][y] += dp[x][y]
                if y + 1 < n:
                    dp[x][y + 1] += dp[x][y]
        return dp[m - 1][n - 1]
