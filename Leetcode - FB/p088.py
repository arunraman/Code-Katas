class p088(object):
    def mergesortedArray(self, nums1, m, nums2, n):
        nums1 += [0] * n
        i , j , last = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                last, i = last - 1, i - 1
            else:
                nums1[last] = nums2[j]
                last, j = last - 1, j - 1

        while j >= 0:
            nums1[last] = nums2[j]
            last, j = last - 1, j - 1
        return nums1


S = p088()
print S.mergesortedArray([1, 10, 100], 3, [4, 6, 7], 3)