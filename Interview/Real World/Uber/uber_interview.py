from collections import Counter, defaultdict


class Solution(object):
    def __init__(self):
        self.longest = 0
        self.word_dict = defaultdict(list)
        self.words_formed = {}

    def read_lines(self, F):
        for line in F:
            line = line.strip()
            if not line:
                continue
            yield line

    def longest_word(self, word_list_1, word_list):
        # if os.path.exists(file):
        #    with open (file) as F:
        #       for line in read_lines(F):
        for word in word_list_1:
            # word_from_file = line.split("\n")
            C = Counter(word_list)
            word_from_file = word
            temp_counter = self.check_longest_word(C, word_from_file)
            self.longest = max(self.longest, temp_counter)
            self.word_dict[temp_counter].append(word_from_file)

        if self.longest != 0:
            return self.word_dict[self.longest]
        else:
            return None


    def check_longest_word(self, counter, word_from_file):
        longest_counter = 0
        for char in word_from_file:
            if char not in counter.keys() or counter[char] <= 0:
                return -1
            else:
                counter[char] -= 1
                longest_counter += 1
        return longest_counter


S = Solution()

print S.longest_word("""
scabs
scab
abba
bbbsc
bacca
ab
""".split("\n"), 'aabbscb')