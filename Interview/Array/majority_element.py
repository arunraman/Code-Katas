from collections import defaultdict
def majority_element(array):
    lookup = defaultdict(int)
    result = set()
    for i in xrange(len(array)):
        if array[i] in lookup:
            lookup[array[i]] += 1
            if lookup[array[i]] >= len(array) // 2:
                result.add(array[i])
        else:
            lookup[array[i]] = 1
    print list(result)

majority_element([1, 2, 3, 1, 2])