def countSmaller_1(arr):
    result = []
    for j in xrange(len(arr)):
        result.append(sum(i < arr[j] for i in arr[j:]))
    return result


def countSmaller_2(nums):
    def sort(enum):
        half = len(enum) / 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller


print countSmaller_1([5, 2, 6, 3, 1])
print countSmaller_2([5, 2, 6, 3, 1])