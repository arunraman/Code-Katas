class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}

    def ladderLength(self, beginWord, endWord, wordDict):
        from collections import defaultdict, deque
        queue = deque([[beginWord, 1]])
        visited = set([beginWord])
        neighbors = defaultdict(list)
        for word in wordDict:
            for x in range(len(word)):
                token = word[:x] + '_' + word[x+1:]
                neighbors[token] += word,
        while queue:
            word, length = queue.popleft()
            if self.wordDist(word, endWord) <= 1:
                return length + 1
            for x in range(len(word)):
                token = word[:x] + '_' + word[x+1:]
                for ladder in neighbors[token]:
                    if ladder not in visited:
                        visited.add(ladder)
                        queue += [ladder, length + 1],
        return 0

    def wordDist(self, wordA, wordB):
        return sum([wordA[x] != wordB[x] for x in range(len(wordA))])

S = Solution()
start = "hit"
end = "cog"
dict = ["hot", "dot", "dog", "lot", "log"]
print S.ladderLength(start, end, dict)
