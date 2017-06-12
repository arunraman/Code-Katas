class Solution(object):
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.findKth(A, B, l // 2)
        else:
            return (self.findKth(A, B, l // 2 - 1) + self.findKth(A, B, l // 2)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = (B, A)
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])

        i = min(len(A) - 1, k / 2)
        j = min(len(B) - 1, k - i)

        if A[i] > B[j]:
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)


S = Solution()
print S.findMedianSortedArrays([1, 12, 15.5, 26, 38], [2, 13, 17, 30, 45])
print S.findMedianSortedArrays([], [2, 13, 17, 30, 45, 50])
print S.findMedianSortedArrays([1, 12, 15], [])


