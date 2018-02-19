from collections import Counter

class p076(object):
    def minwindowSubstring(self, S, T):
        need, missing = Counter(T), len(T)
        i , start, end = 0, 0, 0
        for j, c in enumerate(S, 1):
            if need[c] < 0:
                missing -= 1
            need[c] -= 1
            if not missing:
                while i < j and need[S[i]] < 0:
                    need[S[i]] += 1
                    i += 1
                if not end or j - i <= end - start:
                    start, end = i, j
        return S[start:end]

S = p076()
print S.minwindowSubstring('ADOBECODEBANC', 'ABC')