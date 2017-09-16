import collections

def majority_element(array):
    lookup = collections.defaultdict(int)
    result = set()
    for i in xrange(len(array)):
        if array[i] in lookup:
            lookup[array[i]] += 1
            if lookup[array[i]] >= len(array) // 2:
                result.add(array[i])
        else:
            lookup[array[i]] = 1
    print list(result)

def majorityElement2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return [i[0] for i in collections.Counter(nums).items() if i[1] > len(nums) / 3]


majority_element([1, 2, 3, 1, 2])
print majorityElement2([1, 1, 2, 4, 5])