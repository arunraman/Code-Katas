class Solution(object):
    def countNegatives(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        i = 0
        j = cols - 1
        while j >= 0 and i < rows:
            if grid[i][j] < 0:
               count += (j + 1)
               i += 1
            else:
                j -= 1
        return count


S = Solution()
grid = [[-3, -2, -1 ,1],
        [-2, 2, 3, 4],
        [4, 5, 7, 8]]

print S.countNegatives(grid)