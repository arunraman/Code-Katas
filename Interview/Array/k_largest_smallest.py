import random
def kth_largest_element(nums, k):
    if k > len(nums):
        return False
    pivot = random.choice(nums)
    nums1, nums2 = [], []
    for x in nums:
        if x > pivot:
            nums1.append(x)
        elif x < pivot:
            nums2.append(x)
    if k <= len(nums1):
        return kth_largest_element(nums1, k)
    if k > len(nums) - len(nums2):
        return kth_largest_element(nums2, k - (len(nums) - len(nums2)))
    return pivot

def kth_smallest_element(nums, k):
    if k > len(nums):
        return False
    pivot = random.choice(nums)
    nums1 , nums2 = [], []
    for x in nums:
        if x < pivot:
            nums1.append(x)
        elif x > pivot:
            nums2.append(x)
    if k <= len(nums1):
        return kth_smallest_element(nums1, k)
    if k > len(nums) - len(nums2):
        return kth_smallest_element(nums2, k - (len(nums) - len(nums2)))
    return pivot



print kth_largest_element([3,2,1,5,6,4], 2)
print kth_smallest_element([3,2,1,5,6,4], 2)