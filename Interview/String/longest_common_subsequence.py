def longest_common_sub_sequence(str_1, str_2):
    m = len(str_1)
    n = len(str_2)
    counter = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]
    longest = 0
    lcs_set = set()
    for i in xrange(m):
        for j in xrange(n):
            if str_1[i] == str_2[j]:
                c = counter[i][j] + 1
                counter[i + 1][j + 1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(str_1[i - c + 1:i + 1])
                elif c == longest:
                    lcs_set.add(str_1[i - c + 1:i + 1])
    return lcs_set.pop()

print longest_common_sub_sequence("abcd", "abace")


def longest_common_sequence(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + longest_common_sequence(X, Y, m - 1, n - 1)
    else:
        return max(longest_common_sequence(X, Y, m, n - 1), longest_common_sequence(X, Y, m - 1, n))

X = "abc"
Y = "ac"
print longest_common_sequence(X, Y, len(X), len(Y))