import random
from collections import defaultdict
class dna(object):
    def __init__(self, n):
        self.sequence = "".join(x for x in [random.choice(['A', 'C', 'G', 'T']) for i in xrange(0,n)])
        self.dic = {"A": 1, "C": 2, "G": 3, "T": 4}

    def findRepeatedDnaSequences(self):
        res = []
        dicDNA = defaultdict(int)
        num = 1
        for i in xrange(len(self.sequence)):
            num = (num * 4 + self.dic[self.sequence[i]]) & 0XFFFFF
            if i < 9:
                continue
            if num not in dicDNA:
                dicDNA[num] = 1
            else:
                dicDNA[num] += 1
                if dicDNA[num] == 2:
                    res.append(self.sequence[i - 9:i + 1])

        return res

d = dna(10000)
print d.findRepeatedDnaSequences()
