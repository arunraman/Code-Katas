def edit_distance(str1, str2):
    m = len(str1) + 1
    n = len(str2) + 1
    T = [[0 for x in xrange(n)] for x in xrange(m)]
    for i in xrange(n):
        T[0][i] = i

    for i in xrange(m):
        T[i][0] = i

    for i in range(1, m):
        for j in range(1, n):
            if str1[i - 1] == str2[j - 1]:
                T[i][j] = T[i - 1][j - 1]
            else:
                T[i][j] = 1 + min(T[i - 1][j - 1], T[i - 1][j], T[i][j - 1])

    return T[m - 1][n - 1]


print edit_distance("CAT", "AET")
