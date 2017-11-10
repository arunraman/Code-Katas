from collections import deque


class Solution(object):
    def wordLadder1(self, beginWord, endWord, wordList):
        wordDict = self.constructDict(wordList | set([beginWord, endWord]))
        queue, visited = deque([(beginWord, 1)]), set()
        while queue:
            word, steps = queue.popleft()
            if word not in visited:
                visited.add(word)
                if word == endWord:
                    return steps
                for i in xrange(len(word)):
                    s = word[:i] + '_' + word[i + 1:]
                    neighList = wordDict.get(s, [])
                    for neigh in neighList:
                        if neigh not in visited:
                            queue.append((neigh, steps + 1))
        return 0

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
wordList = ["hot", "dot", "dog", "lot", "log"]
print S.wordLadder1(start, end, set(wordList))
