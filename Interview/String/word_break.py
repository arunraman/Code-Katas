class Solution():
    def wordBreak_1(self, s, wordDict):
        n = len(s)
        dp = [False for i in range(n + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            for w in wordDict:
                if dp[i - len(w)] and s[i - len(w):i] == w:
                    dp[i] = True
        return dp[-1]

    def wordBreak_2(self, s, wordDict):
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if not s:
            return []
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res

S = Solution()
print S.wordBreak_1("leetcode", ["leet", "code"])
print S.wordBreak_2("catsanddog",  ["cat", "cats", "and", "sand", "dog"])