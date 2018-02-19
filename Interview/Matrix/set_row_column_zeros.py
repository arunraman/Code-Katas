class Solution(object):
    def setrowZeros(self, matrix):
        for i in xrange(len(matrix)):
            foundZero = False
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0 and not foundZero:
                    self.setRZeros(i, j - 1, matrix)
                    foundZero = True
                elif matrix[i][j] == 1 and foundZero:
                    matrix[i][j] = 0
        return matrix

    def setRZeros(self, i, j, matrix):
        while j >= 0:
            matrix[i][j] = 0
            j -= 1

    def setcolZeros(self, matrix):
        for j in xrange(len(matrix[0])):
            foundZero = False
            for i in xrange(len(matrix)):
                if matrix[i][j] == 0 and not foundZero:
                    self.setCZeros(i - 1, j, matrix)
                    foundZero = True
                elif matrix[i][j] == 1 and foundZero:
                    matrix[i][j] = 0
        return zip(*matrix)

    def setCZeros(self, i, j, matrix):
        while i >= 0:
            matrix[i][j] = 0
            i -= 1



matrix = [
         [1, 0, 1, 0, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0]
        ]

S = Solution()
print S.setcolZeros(matrix)
