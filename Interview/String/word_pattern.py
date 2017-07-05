class Solution(object):
    def wordPattern_1(self, s, p):
        t = p.split()
        return len(
            set(zip(s, t))) == len(
            set(s)) == len(
            set(t)) and len(s) == len(t)

    def wordPattern_2(self, s, p):
        return self.dfs(s, p, {})

    def dfs(self, s, p, dict):
        if len(s) == 0 and len(p) > 0:
            return False
        if len(s) == len(p) == 0:
            return True
        for end in range(1, len(p)-len(s)+2): # +2 because it is the "end of an end"
            if s[0] not in dict and p[:end] not in dict.values():
                dict[s[0]] = p[:end]
                if self.dfs(s[1:], p[end:], dict):
                    return True
                del dict[s[0]]
            elif s[0] in dict and dict[s[0]] == p[:end]:
                if self.dfs(s[1:], p[end:], dict):
                    return True
        return False


S = Solution()
print S.wordPattern_1("abba", "dog cat cat dog")
print S.wordPattern_2("aba", "abcxyzabr")
print S.wordPattern_2("aabb", "xyzabcxzyabc")
