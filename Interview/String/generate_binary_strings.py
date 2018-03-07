class Solution(object):
    def __init__(self):
        self.binary_stings = []

    def generateSting(self, binary_string, N):
        if N == 0:
            self.binary_stings.append(binary_string)
        else:
            self.generateSting(binary_string + "0", N - 1)
            self.generateSting(binary_string + "1", N - 1)

S = Solution()
S.generateSting("", 3)
print S.binary_stings