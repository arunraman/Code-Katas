class Solution(object):
    def maxProduct(self, words):
        test = {}
        for w in words:
            tmp = 0x0
            for ch in set(w):
                tmp |= (0x1 << (ord(ch) - ord('a')))
            test[tmp] = max(test.get(tmp, 0), len(w))
        return test[tmp]
S = Solution()
print S.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])