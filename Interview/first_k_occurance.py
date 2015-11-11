#!/usr/bin/python
'''
first occurance of k in a sorted array
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


def first_k_occurance(array, k):
    occurance = bin_search(array, k)
    if occurance != -1:
        while occurance > 0:
            if array[occurance - 1] == k:
                occurance -= 1
            else:
                return occurance
        return occurance
    return -1


def Main():
    array = [1, 2, 2, 5, 6, 9, 12]
    print first_k_occurance(array, 2)


if __name__ == '__main__':
        Main()