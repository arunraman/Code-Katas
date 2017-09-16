class doubleQuote(object):

    # Actual line by line content of a file "example.csv"
    # "ColumnA", Column B
    # # "a", b
    # # c, ", d"
    # # e, "\\\'t"
    # # ", d", "\'t"

    # Array of arrays of string to return
    # [["ColumnA", "Column B"],
    # # ["a", "b"],
    # # ["c",  ", d"],
    # ["e, "\'t"]]

    def solution(self, str):
        result = []
        s_1 = str.splitlines()
        res = []
        for s_2 in s_1:
            s_3 = s_2.strip()
            for i in s_3.split(','):
                j = i.strip()
                c = list(i)
                if c[0] == "\"" and c[len(c) - 1] == "\"":
                    res.append(j)
                else:
                    res.append(j)
            result.append(res)
            res = []

        for x in result:
            print x

    def solution2(self):
        res = []
        temp_res = []
        with open('uber.txt') as F:
            lines = F.readlines()
            for line in lines:
                words = line.strip().split(",")
                for word in words:
                    temp_res.append(self.removeDoubleqoutes(word))
                res.append(temp_res)
                temp_res = []
        print res

    def removeDoubleqoutes(self, string):
        if string.startswith("\"") and string.endswith("\""):
            return string[1:-1]
        else:
            return string


# D = doubleQuote()
# D.solution('''"ColumnA", Column B
#         "a", b
#         c, ", d"
#         ", d", "\'t"''')


from collections import defaultdict
class queryMin(object):

    # Given an array find the index of the element with the minimum value between the two given, valid indices in that array.
    #
    # (ex)
    # arr = [-2, 7, -4, 5, 8, 2, 10]
    # index:  0, 1,  2, 3, 4, 5, 6
    #
    # Query(2, 4) returns 2
    # Query(4, 6) returns 5
    #
    # You are allowed to pre-process the array and a build a data structure of your choice.
    # The overall goal is to make Query() function as fast as possible.

    def __init__(self):
        self.array = [-2, 7, -4, 5, 8, 2, 10]
        self.min_lookup = defaultdict(list)

    def find_min(self, index1, index2):
        if index1 == index2 or index1 > index2:
            return 0
        return self.array.index(min(self.array[index1:index2+1]))


    def processArray(self):
        for i in xrange(len(self.array)):
            for j in xrange(len(self.array)):
                self.min_lookup[self.array[i]].append(self.find_min(i, j))


    def Query(self, index1, index2):
        self.processArray()
        print self.min_lookup[self.array[index1]][index2]


Q = queryMin()
Q.Query(2, 4)
Q.Query(4, 6)

import heapq
class klargestsumPair(object):

    def __init__(self):
        self.arr_1 = [2, 3, 5, 8, 13]
        self.arr_2 = [4, 8, 12, 16]
        self.heap = []

    def generatesumPairs(self):
        for i in self.arr_1:
            for j in self.arr_2:
                heapq.heappush(self.heap, ((i + j), (i, j)))
        heapq.heapify(self.heap)


    def getkthMax(self, k):
        if k <= len(self.heap):
            print self.heap[-k]


k = klargestsumPair()
k.generatesumPairs()
k.getkthMax(1)

