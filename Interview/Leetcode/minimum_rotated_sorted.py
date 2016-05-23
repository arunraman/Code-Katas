class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        L = 0; R = len(num)-1
        while L < R and num[L] >= num[R]:
            M = (L+R)/2
            if num[M] > num[L]:
                L = M + 1
            elif num[M] < num[R]:
                R = M
            else:
                L += 1
        return num[L]

class Solution_1:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        L = 0; R = len(num)-1
        while L < R and num[L] > num[R]:
            M = (L+R)/2
            if num[M] < num[R]:
                R = M
            else:
                L = M+1
        return num[L]

S = Solution()
S_1 = Solution_1()
a = [4, 5, 6, 7, 0, 1, 2]
print S.findMin(a)
print S_1.findMin(a)