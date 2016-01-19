#!/usr/bin/python


def three_sum(array, sum):
    if array is None or len(array) < 3:
        return False
        if sum is None:
            return False
        hash_map = {}
        for i in xrange(len(array)):
            for j in xrange(i, len(array)):
                tmp = sum - (array[i] + array[j])
                if tmp not in hash_map:
                    hash_map[tmp] = (i, j)

        for i, e in enumerate(array):
            if e in hash_map and i not in hash_map[e]:
                return hash_map[e], i


def Main():
    array = [0, 1, 5, 9, 1, 10, 11, 3, -15, -4, 2, 0, -6, 7, ]
    position, third_num = three_sum(array, 2)
    for p in position:
        print array[p]
    print third_num

if __name__ == '__main__':
    Main()
