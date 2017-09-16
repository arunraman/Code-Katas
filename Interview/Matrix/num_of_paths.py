


class Solution(object):
    # This uses DP approach
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

    # Count the possible paths from top left to bottom right of a mXn matrix
    def num_paths_matrix_recursive(self, rows, cols):
        if rows == 1 or cols == 1:
            return 1
        return self.num_paths_matrix_recursive(rows - 1, cols) \
               + self.num_paths_matrix_recursive(rows, cols - 1)


S = Solution()
print S.uniquePaths(3, 3)
print S.num_paths_matrix_recursive(3, 3)