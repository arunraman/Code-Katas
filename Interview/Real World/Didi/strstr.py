class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        if m == 0 and n == 0:
            return 0
        if m < n:
            return -1
        for i in xrange(m):
            j = 0
            while j < n:
                if i+j == m:
                    return -1
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            if j == n:
                return i
        return -1