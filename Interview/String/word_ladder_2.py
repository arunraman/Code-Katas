import collections


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordDict = self.constructDict(set(wordList) | set([beginWord, endWord]))
        wordSet = set([])
        for word in wordList:
            wordSet.add(word)

        level = set([beginWord])

        parents = collections.defaultdict(set)

        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                for i in range(len(beginWord)):
                    s = word[:i] + '_' + word[i + 1:]
                    childwordList = wordDict.get(s, [])
                    for childWord in childwordList:
                        if childWord in wordSet and childWord not in parents:
                            next_level[childWord].add(word)
            level = next_level
            parents.update(next_level)

        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p] + r for r in res for p in parents[r[0]]]

        return res

    def constructDict(self, wordList):
        d = {}
        for word in wordList:
            for i in xrange(len(word)):
                s = word[:i] + '_' + word[i + 1:]
                d[s] = d.get(s, []) + [word]
        return d


S = Solution()
start = "hit"
end = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print S.findLadders(start, end, wordList)