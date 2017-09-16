import re

class Matching(object):
    def regularexpresssionMatching(self, s, p):
        # '.' Matches any single character.
        # '*' Matches zero or more of the preceding element.

        result = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]

        result[0][0] = True

        for i in xrange(2, len(p) + 1):
            if p[i - 1] == '*':
                result[0][i] = result[0][i - 2]

        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j - 1] != '*':
                    result[i][j] = result[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                else:
                    result[i][j] = result[i][j - 2] or (result[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

        return result[len(s)][len(p)]

    def wildcardMatching(self, s, p):
        # '?' Matches any single character.
        # '*' Matches any sequence of characters (including the empty sequence).
        p = re.sub(r'\*+', '*', p)

        result = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]

        result[0][0] = True
        for i in xrange(1, len(p) + 1):
            if p[i - 1] == '*':
                result[0][i] = result[0][i - 1]


        for i in xrange(1, len(s) + 1):
            result[i][0] = False
            for j in xrange(1, len(p) + 1):
                if p[j - 1] != '*':
                    result[i][j] = result[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
                else:
                    result[i][j] = result[i][j - 1] or result[i - 1][j]

        return result[len(s)][len(p)]


R = Matching()
# # print R.wildcardMatching("abc", "a**b**c")
# # print R.wildcardMatching("aa", "?")
# # print R.regularexpresssionMatching("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
# print R.regularexpresssionMatching("aa", ".*")
