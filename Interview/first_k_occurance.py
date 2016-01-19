#!/usr/bin/python
'''
first occurrence of k in a sorted array
'''


def bin_search(array, k):
    begin = 0
    end = len(array)
    while begin + 1 < end:
        mid = begin + (end - begin) / 2
        if array[mid] == k:
            return mid
        elif array[mid] > k:
            end = mid
        else:
            begin = mid
    return -1


def first_k_occurrence(array, k):
    occurrence = bin_search(array, k)
    if occurrence != -1:
        while occurrence > 0:
            if array[occurrence - 1] == k:
                occurrence -= 1
            else:
                return occurrence
        return occurrence
    return -1


def Main():
    array = [1, 2, 2, 5, 6, 9, 12]
    print first_k_occurrence(array, 2)


if __name__ == '__main__':
    Main()
