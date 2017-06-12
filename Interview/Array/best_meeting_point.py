def minTotalDistance(grid):
    row_sum = map(sum, grid)
    col_sum = map(sum, zip(*grid))

    def minTotalDistance1D(vec):
        i, j = -1, len(vec)
        distance = left = right = 0
        while i != j:
            if left < right:
                distance += left
                i += 1
                left += vec[i]
            else:
                distance += right
                j -= 1
                right += vec[j]
        return distance

    return minTotalDistance1D(row_sum) + minTotalDistance1D(col_sum)

def minTotalDistance2(grid):
    distance = 0
    for grid in grid, zip(*grid):
        X = []
        for i, val in enumerate(grid):
            X += [i] * sum(val)
            # X[len(X)/2] is nothing but the median
        distance += sum(abs(x - X[len(X)/2]) for x in X)
    return distance

grid = [[1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
       ]

print minTotalDistance(grid)
print minTotalDistance2(grid)