

class Solution(object):
    def getColums(self, grid):
        # * .. unpacking
        return zip(*grid)

    def getRows(self, grid):
        return [[c for c in r] for r in grid]

    def get_backward_diagonals(self, grid):
        b = [None] * (len(grid) - 1)
        grid = [b[i:] + r + b[:i] for i, r in enumerate(self.getRows(grid))]
        return [[c for c in r if not c is None] for r in self.getColums(grid)]

    def get_forward_diagonals(self, grid):
        b = [None] * (len(grid) - 1)
        grid = [b[:i] + r + b[i:] for i, r in enumerate(self.getRows(grid))]
        print grid
        return [[c for c in r if not c is None] for r in self.getColums(grid)]


# def printZMatrix(matrix):
#     i = 0
#     j = 0
#     m = len(matrix)
#     n = len(matrix[0])
#     ret = []
#
#     up = True
#     for _ in xrange(m * n):
#         ret.append(matrix[i][j])
#         if up:
#             if i - 1 < 0 or j + 1 >= n:
#                 up = False
#                 if j + 1 >= n:  # go down
#                     i += 1
#                 else:  # go right
#                     j += 1
#             else:
#                 i -= 1
#                 j += 1
#         else:
#             if i + 1 >= m or j - 1 < 0:
#                 up = True
#                 if i + 1 >= m:
#                     j += 1  # go right
#                 else:
#                     i += 1  # go up
#             else:
#                 i += 1
#                 j -= 1
#
#     return ret





matrix = [['a', 'b', 'c', 'd'],
          ['e', 'f', 'g', 'h'],
          ['i', 'j', 'k', 'l'],
          ['m', 'n', 'o', 'p']]

seen = [[False for j in xrange(len(matrix[0]))] for i in xrange(len(matrix))]

for i in xrange(len(matrix)):
    for j in xrange(len(matrix[0])):
        if seen[i][j] == False:
            k = 0
            temp = ""
            while(i + k < len(matrix) and j + k < len(matrix[0])):
                seen[i+k][j+k] = True
                temp += " ".join(matrix[i+k][j+k])
                k += 1
            print temp


grid = [['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h'],
        ['i', 'j', 'k', 'l'],
        ['m', 'n', 'o', 'p']]

def findDiagonalOrder(matrix):
    m, n = len(matrix), len(matrix and matrix[0])
    return [matrix[i][d-i]
            for d in range(m+n-1)
            for i in range(max(0, d-n+1), min(d+1, m))[::d%2*2-1]]

print findDiagonalOrder(grid)
#S = Solution()

#print S.get_backward_diagonals(matrix)

#print printZMatrix(matrix)

