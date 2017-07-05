import re

class Solution():
    def validWordAbbreviation(self, word, abbr):
        return bool(re.match(re.sub('([1-9]\d*)', r'.{\1}', abbr) + '$', word))


S = Solution()
print S.validWordAbbreviation("internationalization", "i12iz4n")