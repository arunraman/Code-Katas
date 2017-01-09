class WordDistance1:
    def word_distance(self, words, word1, word2):
        distance = float("inf")
        i, index1, index2 = 0, None, None
        while i < len(words):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i
            if index1 is not None and index2 is not None:
                distance = min(distance, abs(index1 - index2))
            i += 1
        print distance

W_1 = WordDistance1()
W_1.word_distance(["practice", "makes", "perfect", "coding", "makes"],
              "coding",
              "practice"
              )

from collections import defaultdict
class WordDistance2:


    def __init__(self, words):
        self.wordindex = defaultdict(list)
        for i in xrange(len(words)):
            self.wordindex[words[i]].append(i)

    def shortest(self, word1, word2):
        index_1 = self.wordindex[word1]
        index_2 = self.wordindex[word2]

        i, j, distance = 0, 0, float("inf")

        while i < len(index_1) and j < len(index_2):
            distance = min(distance, abs(index_1[i] - index_2[j]))
            if index_1[i] < index_2[j]:
                i += 1
            else:
                j += 1
        return distance

W_2 = WordDistance2(["practice", "makes", "perfect", "coding", "makes"])
print W_2.shortest("makes", "coding")


#both words can wbe same
class WordDistance3:
    def shortest(self, words, word1, word2):
        distance = float("inf")
        i , index_1, index_2 = 0, None, None
        while i < len(words):
            if words[i] == word1:
                if index_1 is not None:
                    distance = min(distance, abs(index_1 - i))
                index_1 = i
            elif words[i] == word2:
                index_2 = i
            if index_1 is not None and index_2 is not None:
                distance = min(distance, abs(index_1 - index_2))
            i += 1
        print distance

W_3 = WordDistance3()
W_3.shortest(["practice", "makes", "perfect", "coding", "makes"],
              "makes",
              "makes")
