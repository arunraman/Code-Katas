class p0349(object):
    def intersectiontwoArrays(self, nums1, nums2):
        result = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if not (len(result) and nums1[i] == result[len(result) - 1]):
                    result.append(nums1[i])
                i += 1
                j += 1

        return result

S = p0349()
print S.intersectiontwoArrays([1, 2, 2, 1], [2, 2])
