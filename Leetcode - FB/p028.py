class p028(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

S = p028()
print S.strStr("hello", "ll")
print S.strStr("aaaaa", "bba")