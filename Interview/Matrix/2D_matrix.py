import itertools
class Solution():
    def combination_of_arrays(self, input):
        return [each for each in itertools.product(*input)]

    def rotate_matrix(self, grid):
        return [list(reversed(i)) for i in zip(*grid)]

    def spiralOrder1(self, grid):
        return grid and list(grid.pop(0)) + self.spiralOrder1(zip(*grid)[::-1])

    def spiralOrder2(self, n):
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + zip(*A[::-1])
        return A

    def setZeroes(self, grid):
        # First row has zero?
        m, n, firstRowHasZero = len(grid), len(grid[0]), not all(grid[0])

        # Use first row/column as marker, scan the matrix
        for i in xrange(1, m):
            for j in xrange(n):
                if grid[i][j] == 0:
                    grid[0][j] = grid[i][0] = 0

        # Set the zeros
        for i in xrange(1, m):
            for j in xrange(n - 1, -1, -1):
                if grid[i][0] == 0 or grid[0][j] == 0:
                    grid[i][j] = 0

        # Set the zeros for the first row
        if firstRowHasZero:
            grid[0] = [0] * n



S = Solution()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_2 = [[1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0],
            [1, 1, 1, 1]]


print S.combination_of_arrays([[1, 2, 3], [1], [1, 2]])


print S.rotate_matrix(matrix)
print S.spiralOrder1(matrix)
print S.spiralOrder2(3)


S.setZeroes(matrix_2)
print matrix_2