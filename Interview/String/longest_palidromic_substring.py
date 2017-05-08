class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in xrange(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)
        return res

    def helper(self, s, left, right):
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

S = Solution()
print S.longestPalindrome("abbaa")