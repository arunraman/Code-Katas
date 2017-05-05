def rotate_matrix(grid):
    return [list(reversed(i)) for i in zip(*grid)]

def spiralOrder1(grid):
    return grid and list(grid.pop(0)) + spiralOrder1(zip(*grid)[::-1])

def spiralOrder2(n):
    A, lo = [], n*n+1
    while lo > 1:
        lo, hi = lo - len(A), lo
        A = [range(lo, hi)] + zip(*A[::-1])
    return A

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print rotate_matrix(matrix)
print spiralOrder1(matrix)
print spiralOrder2(3)