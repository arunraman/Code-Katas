# minimum window substring

from collections import Counter

def minWindow(s, t):
    need, missing = Counter(t), len(t)
    i = start = end = 0
    for j, c in enumerate(s, 1):
        if need[c] > 0:
            missing -= 1
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not end or j - i <= end - start:
                start, end = i, j
    return s[start:end]

print minWindow('ADOBECODEBANC', 'ABC')