#!/usr/bin/python
import random


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}

    def findKthLargest(self, nums, k):
        if k > len(nums):
            return False
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot

    def findKthSmallest(self, nums, k):
        if k > len(nums):
            return False
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for num in nums:
            if num < pivot:
                nums1.append(num)
            elif num > pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthSmallest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthSmallest(nums2, k - (len(nums) - len(nums2)))
        return pivot


def Main():
    a = [5, 4, 7, 1, 2]
    S = Solution()
    print S.findKthLargest(a, 1)
    print S.findKthSmallest(a, 6)

if __name__ == '__main__':
    Main()
