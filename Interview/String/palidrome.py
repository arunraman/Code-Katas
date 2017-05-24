import re, collections, itertools

class Solution(object):

    def validPalindrome(self, s):
        new_str = "".join(re.findall(r'[a-z0-9]', s.lower(), re.I))
        for i, j in zip(xrange(len(new_str) / 2), xrange(len(new_str) - 1, len(new_str) / 2 - 1, -1)):
            if new_str[i] != new_str[j]:
                return False
        return True

##############################################################################

    def longestPalindromeUpperLowerLetter(self, s):
        odd = sum(map(lambda x: x == 1 , collections.Counter(s).values()))
        return len(s) - odd + int(odd > 0)


    def longestPalindromeSubstring(self, s):
        res = ""
        for i in xrange(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)
        return res

    def helper(self, s, left, right):
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

##############################################################################

    def palindromePairs(self, words):
        d, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
        pairs = []
        for i, w in enumerate(words):
            for j in xrange(len(w) + 1):
                prefix, postfix = w[:j], w[j:]
                if prefix in d and i != d[prefix] and postfix == postfix[::-1]:
                    res.append([i, d[prefix]])
                    pairs.append(words[i] + words[d[prefix]])
                if j > 0 and postfix in d and i != d[postfix] and prefix == prefix[::-1]:
                    res.append([d[postfix], i])
                    pairs.append(words[d[postfix]] + words[i])
        return res, pairs

##############################################################################

    def nearestPalindromic(self, n):
        l = len(n)
        # with different digits width, it must be either 10...01 or 9...9
        candidates = set((str(10 ** l + 1), str(10 ** (l - 1) - 1)))
        # the closest must be in middle digit +1, 0, -1, then flip left to right
        prefix = int(n[:(l + 1) / 2])
        for i in map(str, (prefix - 1, prefix, prefix + 1)):
            candidates.add(i + [i, i[:-1]][l & 1][::-1])
        candidates.discard(n)
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))

##############################################################################

    def palindromePartition1(self, s):
        ret = []
        for i in xrange(1, len(s) + 1):
            if s[:i] == s[i - 1::-1]:
                for rest in self.palindromePartition1(s[i:]):
                    ret.append([s[:i]] + rest)
        if not ret:
            return [[]]
        return ret

    def palindromePartition2(self, s):
        lookup = [[False for j in xrange(len(s))] for i in xrange(len(s))]
        mincut = [len(s) - 1 - i for i in xrange(len(s) + 1)]

        for i in reversed(xrange(len(s))):
            for j in xrange(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                    mincut[i] = min(mincut[i], mincut[j + 1] + 1)

        return mincut[0]

##############################################################################


    def palindromePermutation1(self, s):
        # "code" -> False, "aab" -> True, "carerac" -> True.
        return sum(v % 2 for v in collections.Counter(s).values()) < 2

    def palindromePermutation2(self, s):
        # Given s = "aabb", return ["abba", "baab"].
        # Given s = "abc", return [].
        cnt = collections.Counter(s)
        mid = tuple(k for k, v in cnt.iteritems() if v % 2)
        chars = ''.join(k * (v / 2) for k, v in cnt.iteritems())
        return [''.join(half_palindrome + mid + half_palindrome[::-1]) \
                for half_palindrome in set(itertools.permutations(chars))] if len(mid) < 2 else []

##############################################################################

S = Solution()

# Valid Palindrome
print S.validPalindrome("A man, a plan, a canal: Panama")
print S.validPalindrome("race a car")

print "\n"

# Longest Palindrome
print S.longestPalindromeUpperLowerLetter("Aa")
print S.longestPalindromeSubstring("babbad")

print "\n"

# Palindrome paris
print S.palindromePairs(["bat", "tab", "cat"])
print S.nearestPalindromic("121")

print "\n"

# Palindrome Partition
print S.palindromePartition1("aab")
print S.palindromePartition2("axt")

print "\n"


# Palindrome Permutations
print S.palindromePermutation1("aab")
print S.palindromePermutation2("aab")