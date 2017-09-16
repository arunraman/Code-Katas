class Solution:
    def isMatch(self, str, pat):
        """
        :type str: string
        :type pat: string
        :rtype: bool
        """
        if not pat:
            return not str
        minReps = 1
        maxReps = 1
        closeBraces = 0
        char = pat[0]
        if len(pat) > 1:
            if pat[1] == '{':
                closeBraces = pat.find('}')
                rangeSubstr = pat[2:closeBraces]
                leftStr, rightStr = rangeSubstr.split(',')
                maxReps = int(rightStr)
                minReps = int(leftStr)
                # print(minReps, maxReps)
        cntr = 0
        while cntr < minReps:
            if str[cntr] != char:
                return False
            cntr += 1
        newStr = str[minReps:]
        newPat = pat[closeBraces+1:]
        if maxReps > minReps:
            diff = maxReps - minReps
            for i in range(0, diff):
                newPatDiffed = char*i + newPat
                #print(newPatDiffed, newStr)
                success = self.isMatch(newStr, newPatDiffed)
                if success:
                    return True
            return False
        else:
            return self.isMatch(newStr, newPat)

S = Solution()
print S.isMatch("aa","a") # false
print S.isMatch("aa","aa") # true
print S.isMatch("aaa","aa") # false
print S.isMatch("aa","a{1,3}") # true
print S.isMatch("aaa","a{1,3}") #false
print S.isMatch("ab","a{1,3}b{1,3}")  #true
print S.isMatch("abc","a{1,3}b{1,3}c")  #true
print S.isMatch("abbc","a{1,3}b{1,2}c")  #false
print S.isMatch("acbac","a{1,3}b{1,3}c")  #false
print S.isMatch("abcc","a{1,3}b{1,3}cc{1,3}")  #true