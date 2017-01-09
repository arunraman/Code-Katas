import re


def longest_common_prefix(strs):
    if not strs:
        return ""

    for i in xrange(len(strs[0])):
        for string in strs[1:]:
            if i >= len(string) or string[i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]

print longest_common_prefix(["hello", "heaven", "heavy"])
print longest_common_prefix(["aas", "a"])

def isomorphic_string(str1, str2):
    if len(str1) != len(str2):
        return False
    return len(set(zip(str1, str2))) == len(set(str1)) == len(set(str2))

print isomorphic_string("foo", "boo")


def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))

X = "foo"
Y = "aoo"
print lcs(X, Y, len(X), len(Y))


def strStr(haystack, needle):
    for i in xrange(len(haystack) - len(needle) + 1):
        if haystack[i: i + len(needle)] == needle:
            return i
    return -1

print strStr("abababcdab", "cdab")

def valid_palindrome(str):
    new_str = "".join(re.findall(r'[a-z0-9]', str.lower(), re.I))
    for i , j in zip(xrange(len(new_str)/2), xrange(len(new_str) - 1, len(new_str)/2 - 1, -1)):
        if new_str[i] != new_str[j]:
            return False
    return True

print valid_palindrome("A man, a plan, a canal: Panama")
print valid_palindrome("race a car")

def findSubstringinorder(S, L):
    import re
    substring = ''.join(str for str in L)
    return [(m.start(), m.end()) for m in re.finditer(substring, S)]


def findSubstringanyorder(S, L):
    n, m, w = len(S), len(L), len(L[0])
    result = []
    for index in xrange(n-m*w+1):
        seg = [S[i:i+w] for i in xrange(index, index+m*w, w)]
        for item in L:
            if item in seg:
                seg.remove(item)
            else:
                break
        if seg == []:
            result.append((index, index+m*w))
    return result

S = "barfoobar"
L = ["foo", "bar"]
print findSubstringinorder(S, L)
print findSubstringanyorder(S, L)

# minimum window substring
from collections import Counter
def minWindow(s, t):
    need, missing = Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        if need[c] > 0:
            missing -= 1
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]
print minWindow('ADOBECODEBANC', 'ABC')

