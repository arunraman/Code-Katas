import re


def isomorphic_string(str1, str2):
    if len(str1) != len(str2):
        return False
    return len(set(zip(str1, str2))) == len(set(str1)) == len(set(str2))

print isomorphic_string("foo", "boo")


def strStr(haystack, needle):
    for i in xrange(len(haystack) - len(needle) + 1):
        if haystack[i: i + len(needle)] == needle:
            return i
    return -1

print strStr("abababcdab", "cdab")
