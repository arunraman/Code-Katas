def repeatedSubstringPattern(S):
    return S in (2 * S)[1:-1]

print repeatedSubstringPattern("abab")