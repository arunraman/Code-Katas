from collections import defaultdict

class p049(object):
    def __init__(self):
        self.groupDict = defaultdict(list)
        self.result  = []

    def groupAnagrams(self, strs):
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in self.groupDict:
                self.groupDict[sorted_str] = [str]
            else:
                self.groupDict[sorted_str].append(str)

        for vals in self.groupDict.itervalues():
            self.result.append(sorted(vals))

        return self.result



S = p049()
print S.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])