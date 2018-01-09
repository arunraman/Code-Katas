# Write a function to simulate the `wc` command.
# Input: file path
# Output: the number of words in that file


# dict word as key and count as the value
# /tmp/file.txt


import os
import re
from collections import defaultdict

class Solution(object):

    def __init__(self):
        self.wordDict = defaultdict(int)
        self.total_count = 0

    def read_lines(self, FILE):
        for line in FILE:
            line = line.strip()
            if not line:
                continue
            yield line

    def wordCount(self, file_path):
        if os.path.exists(file_path):
            with open (file_path) as FILE:
                for line in self.read_lines(FILE):
                    words = line.lower()
                    #words = 'foo goo boo bas, asre;'
                    words_list = re.findall(r'\w\.\w\.?|\w+',words)
                    for word in words_list:
                        if word not in self.wordDict:
                            self.wordDict[word] = 0
                        self.wordDict[word] += 1

    def printWords(self):
        print self.wordDict
        for word, count in self.wordDict.iteritems():
            self.total_count += count
        print self.total_count


S = Solution()
S.wordCount('data.txt')
S.printWords()

#nickz@pinterest.com