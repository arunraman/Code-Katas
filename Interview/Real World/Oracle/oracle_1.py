class Solution(object):
    def stringClean(self, strs):
        i = 0
        result = ""
        n = len(strs)
        while i < n:
            if i == n - 1:
                if strs[i] != strs[i - 1]:
                    result += " ".join(strs[i])
                i += 1
            else:
                if strs[i] == strs[i + 1]:
                    i += 1
                else:
                    result += " ".join(strs[i])
                    i += 1
        return result

    def maxBlock(self, strs):
        if len(strs) < 1:
            return 0
        i = 1
        n = len(strs)
        count = 1
        maxCount = 1
        while i < n:
            if strs[i - 1] == strs[i]:
                count += 1
                maxCount = max(count, maxCount)
            else:
                count = 1
            i += 1

        return maxCount

    def reorderBlock(self, strs):
        i = 1
        n = len(strs)
        pass



S = Solution()
print S.stringClean("yyzzza")
print S.stringClean("abbbcdd")
print S.stringClean("Hello")


print S.maxBlock("hoopla")
print S.maxBlock("abbCCCddBBBxx")

print S.reorderBlock("abbCCCddBBBxx")
